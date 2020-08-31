import hashlib, binascii, os, json
from Engine.settings import ConfigFile


class Hashing:
    def __init__(self):
        self.Path = ConfigFile
        self.salt_ln = self.get_salt_length()
        self.password_algo = 'sha512'

    def get_salt_length(self):
        config_file = open(self.Path, 'r')
        config_file = json.loads(config_file.read())
        salt_length = config_file['saltLength']
        return salt_length

    def _create_new_salt(self):
        return hashlib.sha256(os.urandom(self.salt_ln)).hexdigest().encode('ascii')

    def _create_new_hash(self, password, salt):
        pwd_hash = hashlib.pbkdf2_hmac(self.password_algo, password.encode('utf-8'), salt, 100000)
        pwd_hash = binascii.hexlify(pwd_hash)
        pwd_hash = (salt + pwd_hash).decode('ascii')
        return pwd_hash

    def _compare_stored_hash(self, password, salt, old_hash):
        salt = salt.encode()
        pwd_hash = self._create_new_hash(password, salt)
        return pwd_hash == old_hash

    def generate_password(self, password):
        salt_ = self._create_new_salt()
        password_ = self._create_new_hash(password, salt_)
        return password_, salt_.decode()
