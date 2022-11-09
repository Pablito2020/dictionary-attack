import sys
import time

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES128
from cryptography.hazmat.primitives.ciphers.modes import ECB

from src.password import Password
from src.pkcs5 import PKCS5, InvalidPKCS5File


def print_valid_messages(pkcs5: PKCS5, dictionary_path: str):
    for password in Password.get_all_passwords(dictionary_path):
        cipher = Cipher(AES128(password.get_key(pkcs5)), ECB())
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
    try:
        pkcs5_file: PKCS5 = PKCS5.get_from_file("data/exercici.bin")
    except InvalidPKCS5File as ex:
        print(f"Invalid PKCS5 file format. Error: {ex}")
        sys.exit(-1)
    print(pkcs5_file)
    print_valid_messages(pkcs5_file, "data/diccionari.txt")
    final_time: float = time.perf_counter()
    print(f"Program finished in: {final_time - init_time}")
