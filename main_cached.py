import time
from typing import Generator, Tuple

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES128
from cryptography.hazmat.primitives.ciphers.modes import ECB

from src.pkcs5 import PKCS5, get_pkcs5


DICTIONARY = "data/cached_passwords.txt"


def get_passwords(dictionary=DICTIONARY, separator=",") -> Generator[Tuple[str, bytes], None, None]:
    with open(dictionary, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            password, key = line.split(separator)
            key = key.strip()
            yield password, bytes.fromhex(key)


def print_valid_messages(pkcs5: PKCS5):
    for password, key in get_passwords():
        cipher = Cipher(AES128(key), ECB())
        decryptor = cipher.decryptor()
        result = decryptor.update(pkcs5.message) + decryptor.finalize()
        try:
            message = result.decode("utf-8")
            print(f"Message is: {message}")
            print(f"Password is: {password}")
        except UnicodeDecodeError:
            pass


if __name__ == "__main__":
    init_time: float = time.perf_counter()
    pkcs5_file = get_pkcs5()
    print_valid_messages(pkcs5_file)
    final_time: float = time.perf_counter()
    print(f"Program finished in: {final_time - init_time}")
