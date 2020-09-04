import datetime
import json
import os
import jwt
import uuid
from datetime import timedelta
from Models.models import *
from Engine.settings import ConfigFile
from django.db import connection


class JWTClass:
    def __init__(self):
        self.Path = ConfigFile
        self.TokenProvider = self.get_jwt_information()

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

    def get_jwt_model(self, user_session, claims, roles, expiry_date, specification):
        return {
            'aud': self.TokenProvider['tokenAudience'],
            'expiry': expiry_date,
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/sid': str(user_session.UserId.UserId),
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress': user_session.UserId.Username,
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name': [user_session.UserId.Username,
                                                                           user_session.UserId.DisplayName],
            'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/role': roles,
            'https://cms360/claims/culturename': user_session.UserId.Language,
            'iss': self.TokenProvider['tokenIssuer'],
            'specification': specification,
            'sub': user_session.UserId.Username,
            'exp': self.convert_date_time_to_timestamp(user_session.Expiry),
            'nbf': self.convert_date_time_to_timestamp(user_session.CreatedAt)
        }

    def generate_jwt_token(self, user_session, roles, expiry_date, specification):
        data_ = self.get_jwt_model(user_session, [], roles, expiry_date, specification)
        encoded_token = jwt.encode(data_, self.TokenProvider['tokenSecurityKey'],
                                   algorithm=self.TokenProvider['tokenSecurityAlgorithm'])
        encoded_token = encoded_token.decode('utf-8')
        return encoded_token

    @staticmethod
    def response_user_id(us_):
        if us_:
            return us_.UserId
        return False

    def decode_jwt_token(self, token, role_check=None):
        try:
            decoded_token = jwt.decode(token, self.TokenProvider['tokenSecurityKey'],
                                       algorithm=[self.TokenProvider['tokenSecurityAlgorithm']])
            expiry_ = datetime.datetime.fromtimestamp(decoded_token['expiry'])
            if expiry_ > datetime.datetime.now():
                us_ = UserSession.objects.filter(ChallengeCheck=decoded_token['specification'], IsValid=True,
                                                 Expiry=expiry_).last()
                return self.response_user_id(us_)
            return False
        except Exception as e:
            return False

    def decode_jwt_token_and_logout(self, token):
        try:
            decoded_token = jwt.decode(token, self.TokenProvider['tokenSecurityKey'],
                                       algorithm=[self.TokenProvider['tokenSecurityAlgorithm']])
            expiry_ = datetime.datetime.fromtimestamp(decoded_token['expiry'])
            UserSession.objects.filter(ChallengeCheck=decoded_token['specification'],
                                       Expiry=expiry_).update(IsValid=False)
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
        specification = str(self.generate_specification())
        user_session = UserSession.objects.create(UserId=user, Expiry=date, ChallengeCheck=specification)
        return self.generate_jwt_token(user_session, self.get_user_roles(user), timestamp, specification)
