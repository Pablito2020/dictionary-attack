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
