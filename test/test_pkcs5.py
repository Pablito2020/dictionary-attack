from src.pkcs5 import PKCS5


def test_pkcs5_open_file():
    pkcs5: PKCS5 = PKCS5.get_from_file("test/openssl_pkcs5_example.bin")
    assert pkcs5.salt == b"\x10\xf2''lO\xc53"
    assert (
        pkcs5.message
        == b"FL\x088\x149\xb4\xfd`7u\x84\xe1\x8e-\xa0\x84\xb6\xd8\xef\x84\xde+\x93T\xf9\x9fM\xf1\xa0\xeb\x9f"
    )
