"""
This file includes all the operations that we need for the pkcs5 file.
Encapsulates how the file parsing is done, and returns a data object
which has the salt and message in bytes
"""

import sys
from dataclasses import dataclass


class InvalidPKCS5File(Exception):
    pass


@dataclass
class PKCS5:
    salt: bytes
    message: bytes

    @staticmethod
    def get_from_file(file_path: str) -> "PKCS5":
        with open(file_path, "rb") as file:
            file_bytes: bytes = file.read()
            PKCS5._assert_correct_prefix(file_bytes)
            salt = file_bytes[8:16]
            message = file_bytes[16:]
            return PKCS5(salt=salt, message=message)

    @staticmethod
    def _assert_correct_prefix(file: bytes):
        prefix_salt = file[:8]
        if prefix_salt != b"Salted__":
            raise InvalidPKCS5File(f"salt prefix is invalid (not Salted__): {prefix_salt.hex()}")

    def __str__(self) -> str:
        return f"PKCS5: \n[\n\tSalt is: {self.salt.hex()},\n\tMessage is: {self.message.hex()}\n]"

    def __repr__(self) -> str:
        return self.__str__()


def get_pkcs5(file="data/exercici.bin") -> PKCS5:
    try:
        pkcs5_file: PKCS5 = PKCS5.get_from_file(file)
        print(pkcs5_file)
        return pkcs5_file
    except InvalidPKCS5File as ex:
        print(f"Invalid PKCS5 file format. Error: {ex}")
        sys.exit(-1)
