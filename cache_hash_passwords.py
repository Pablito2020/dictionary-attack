import sys

from src.password import Password
from src.pkcs5 import PKCS5, InvalidPKCS5File

if __name__ == "__main__":
    try:
        pkcs5_file: PKCS5 = PKCS5.get_from_file("data/exercici.bin")
    except InvalidPKCS5File as ex:
        print(f"Invalid PKCS5 file format. Error: {ex}")
        sys.exit(-1)
    passwords = list(Password.get_all_passwords("data/diccionari.txt"))
    with open("data/cached_passwords.txt", 'w', encoding='utf-8') as file:
        for password in passwords:
            file.write(f"{str(password)},{password.get_key(pkcs5_file).hex()}\n")
