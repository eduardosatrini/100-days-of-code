from caeser_cipher import CaeserCipher
from pytest import fixture

@fixture
def cipher():
    return CaeserCipher(shift=3)

def test_input_cipher_with_encrypt(cipher):
    
    result = cipher.encrypt("my msg")
    expected = "pb#pvj"
    
    assert result == expected


def test_input_cipher_with_decrypt(cipher):

    result = cipher.decrypt("pb#pvj")
    expected = "my msg"
    
    assert result == expected
