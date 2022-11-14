from src.password import Password
from src.pkcs5 import PKCS5, get_pkcs5

if __name__ == "__main__":
    pkcs5_file: PKCS5 = get_pkcs5("data/exercici.bin")
    passwords = list(Password.get_all_passwords("data/diccionari.txt"))
    with open("data/cached_passwords.txt", "w", encoding="utf-8") as file:
        for password in passwords:
            file.write(f"{str(password)},{password.get_key(pkcs5_file).hex()}\n")
