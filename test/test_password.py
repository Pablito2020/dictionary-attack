from src.password import Password
from src.pkcs5 import PKCS5


def test_password_returns_correct_key():
    password = Password("Yukuo7")
    pkcs5 = PKCS5(salt=bytes.fromhex("10f227276c4fc533"), message=None)
    correct_key = bytes.fromhex("91610b8c5a7a2a11fbc110ba63eea202")
    assert password.get_key(pkcs5) == correct_key


def test_generator_password_returns_all_passwords():
    set_passwords = set(Password.get_all_passwords("test/dictionary_test.txt"))
    set_correct_passwords = {Password("Pablo")}
    for i in range(0, 10):
        set_correct_passwords.add(Password(f"Pablo{i}"))
        for j in range(0, 10):
            set_correct_passwords.add(Password(f"Pablo{i}{j}"))
    assert set_correct_passwords == set_passwords
