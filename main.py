import sys
from dataclasses import dataclass
from typing import Generator

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES128
from cryptography.hazmat.primitives.ciphers.modes import ECB
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def get_all_passwords(dictionary_path: str) -> Generator[bytes, None, None]:
    with open(dictionary_path, "r", encoding="utf-8") as dictionary_file:
        for password in dictionary_file.readlines():
            good_password = password.strip()
            yield good_password.encode("utf-8")
            for first_number in range(0, 10):
                yield f"{good_password}{first_number}".encode("utf-8")
                for second_number in range(0, 10):
                    yield f"{good_password}{first_number}{second_number}".encode("utf-8")


@dataclass
class PKCS5:
    salt: bytes
    message: bytes

    def __str__(self) -> str:
        return f"Salt is: {self.salt.hex()}\nMessage is: {self.message.hex()}"

    def __repr__(self) -> str:
        return self.__str__()


class InvalidPKCS5File(Exception):
    pass


def get_pkcs5(file_path: str) -> PKCS5:
    with open(file_path, "rb") as file:
        file_bytes: bytes = file.read()
        prefix_salt = file_bytes[:8]
        if prefix_salt != b"Salted__":
            raise InvalidPKCS5File(f"salt prefix is invalid (not Salted__): {prefix_salt.hex()}")
        assert prefix_salt == b"Salted__"
        salt = file_bytes[8:16]
        message = file_bytes[16:]
        return PKCS5(salt=salt, message=message)


class Password:
    def __init__(self, password: bytes):
        self.password = password
        kdf = PBKDF2HMAC(
            algorithm=SHA1(),
            length=16,
            salt=pkcs5.salt,
            iterations=1,
        )
        self.key = kdf.derive(password)

    def get_key(self) -> bytes:
        return self.key

    def get_key_hex(self) -> str:
        return self.key.hex()


def get_valid_messages(key_and_message: PKCS5, dictionary_path: str):
    for password in get_all_passwords(dictionary_path):
        passw = Password(password)
        cipher = Cipher(AES128(passw.get_key()), ECB())
        decryptor = cipher.decryptor()
        result = decryptor.update(key_and_message.message) + decryptor.finalize()
        try:
            message_new = result.decode("utf-8")
            print(message_new)
            print(passw.get_key_hex())
            print(f"Message is: {result.decode('utf-8')}")
        except UnicodeDecodeError:
            pass


if __name__ == "__main__":
    try:
        pkcs5 = get_pkcs5("data/exercici.bin")
    except InvalidPKCS5File as ex:
        print(f"Invalid PKCS5 file format. Error: {ex}")
        sys.exit(-1)
    print(pkcs5)
    get_valid_messages(pkcs5, "data/diccionari.txt")
