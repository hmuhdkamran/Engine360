import base64
import hashlib
import os


class Hashing:
    def __init__(self):
        self.salt_ln = 16

    def _create_new_salt(self):
        return os.urandom(self.salt_ln)

    def _create_new_hash(self, password, salt):
        password = password.encode()
        hash_object = hashlib.sha256(password + salt)
        hash_b64 = base64.b64encode(hash_object.digest() + salt)
        return hash_b64

    def _compare_stored_hash(self, password, salt, old_hash):
        salt = salt.encode()
        re_hash = self._create_new_hash(password, salt)
        if re_hash.decode() == old_hash.decode():
            return True
        else:
            return False

    def generate_password(self, password):
        return password, 'salt'
        # salt_ = self._create_new_salt()
        # password_ = self._create_new_hash(password, salt_)
        # return password_, salt_

    def get_old_salt(self, input_hash):
        return base64.b64decode(input_hash)[-self.salt_ln:]

    def validate_password(self, password, salt, hash_pasword):
        if hash_pasword == password:
            return True
        return False
