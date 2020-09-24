import datetime
import json
from datetime import timedelta

import jwt
import redis
from django.conf import settings
from django.db import connection

from Engine.settings import ConfigFile
from Models.models import *

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


class JWTClass:
    def __init__(self):
        self.Path = ConfigFile
        self.TokenProvider = self.get_jwt_information()
        self.SecretKey = self.TokenProvider['tokenSecurityKey']
        self.Algorithm = self.TokenProvider['tokenSecurityAlgorithm']

    @staticmethod
    def generate_specification():
        return uuid.uuid1()

    def get_jwt_information(self):
        config_file = open(self.Path, 'r')
        config_file = json.loads(config_file.read())
        token_provider = config_file['tokenProvider']
        return token_provider

    def get_expiry_date(self):
        date_ = datetime.datetime.now() + timedelta(minutes=int(self.TokenProvider['tokenExpiration']))
        return date_, date_.timestamp()

    @staticmethod
    def convert_date_time_to_timestamp(date_time):
        return int(date_time.timestamp())

    def get_jwt_model(self, user, roles, time_information):
        return {
            'aud': self.TokenProvider['tokenAudience'],
            'expiry': time_information['expiry_date'],
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/sid': str(user.UserId),
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress': user.Username,
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name': [user.Username,
                                                                           user.DisplayName],
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/role': roles,
            'https://engine360/claims/culturename': user.Language,
            'iss': self.TokenProvider['tokenIssuer'],
            'sub': user.Username,
            'typ': 'JWT',
            'exp': time_information['expiry_date'],
            'iat': time_information['created_at']
        }

    def generate_jwt_token(self, user, roles, time_information):
        data_ = self.get_jwt_model(user, roles, time_information)
        encoded_token = jwt.encode(data_, key=self.SecretKey, algorithm=self.Algorithm)
        encoded_token = encoded_token.decode('utf-8')
        return encoded_token

    @staticmethod
    def response_user_id(us_):
        if us_:
            return us_.UserId
        return False

    @staticmethod
    def check_route_and_permission(obj, route_info):
        if obj['RouteName'] == route_info['RouteName'] and obj['Operation'] == route_info['Operation']:
            return True
        return False

    def decode_jwt_token(self, token, route_info=None):
        try:
            decoded_token = jwt.decode(token, key=self.SecretKey, algorithms=self.Algorithm, verify=False)
            expiry_ = datetime.datetime.fromtimestamp(decoded_token['expiry'])

            roles = decoded_token['http://schemas.xmlsoap.org/ws/2005/05/identity/claims/role']
            if route_info:
                if len(list(filter(lambda x: self.check_route_and_permission(x, route_info), roles))) == 0:
                    return False

            if expiry_ > datetime.datetime.now():

                black_list_tokens = redis_instance.get('black_list_tokens')
                if black_list_tokens:
                    block_list_tokens = json.loads(black_list_tokens)
                    if token in block_list_tokens:
                        return False

                user = User.objects.get(
                    UserId=decoded_token['http://schemas.xmlsoap.org/ws/2005/05/identity/claims/sid'])
                return user
            return False
        except Exception as e:
            return False

    def decode_jwt_token_and_logout(self, token):
        try:
            decoded_token = jwt.decode(token, self.TokenProvider['tokenSecurityKey'],
                                       algorithm=[self.TokenProvider['tokenSecurityAlgorithm']], verify=False)
            expiry_ = datetime.datetime.fromtimestamp(decoded_token['expiry'])

            black_list_tokens = redis_instance.get('black_list_tokens')
            if black_list_tokens:
                black_list_tokens = json.loads(black_list_tokens)
                if token in black_list_tokens:
                    return False
            else:
                black_list_tokens = []

            if expiry_ > datetime.datetime.now():
                black_list_tokens.append(token)
                black_list_tokens = json.dumps(black_list_tokens)
                redis_instance.set('black_list_tokens', black_list_tokens)

            return True
        except Exception as e:
            return False

    @staticmethod
    def get_user_roles(user):
        role_query = Queries.objects.filter(FullName='GenerateRole').last()
        if role_query:
            with connection.cursor() as cursor:
                query = role_query.Description.format(user.UserId)
                cursor.execute(query)
                col_desc = cursor.description
                column_names = [col[0] for col in col_desc]
                rows = cursor.fetchall()
                return [dict(zip(column_names, row)) for row in rows]
        return []

    def create_user_session(self, user):
        date, timestamp = self.get_expiry_date()
        created_at = datetime.datetime.now().timestamp()
        time_information = {'expiry_date': timestamp, 'created_at': created_at}
        return self.generate_jwt_token(user, self.get_user_roles(user), time_information)
