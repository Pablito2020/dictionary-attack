from typing import Generator

from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from src.pkcs5 import PKCS5


class Password:
    def __init__(self, password: str):
        self.password = password.encode("utf-8")

    def get_key(self, pkcs5: PKCS5) -> bytes:
        kdf = PBKDF2HMAC(algorithm=SHA1(), length=16, salt=pkcs5.salt, iterations=1)
        return kdf.derive(self.password)

    @staticmethod
    def get_all_passwords(dictionary_path: str) -> Generator["Password", None, None]:
        with open(dictionary_path, "r", encoding="utf-8") as dictionary_file:
            for password in dictionary_file.readlines():
                good_password = password.strip()
                yield Password(good_password)
                for first_number in range(0, 10):
                    yield Password(f"{good_password}{first_number}")
                    for second_number in range(0, 10):
                        yield Password(f"{good_password}{first_number}{second_number}")

    def __str__(self):
        return self.password.decode("utf-8")

    def __repr__(self):
        return self.__str__()
