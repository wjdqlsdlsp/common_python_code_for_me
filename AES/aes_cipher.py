import abc
import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESCipher(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    def encrypt(self, data: str) -> str | None:
        pass

    def decrypt(self, data: str) -> str | None:
        pass


class StaticAESCipher(AESCipher):
    def __init__(self, key: str):
        self.key = key
        self.cipher = AES.new(self.key.encode(), AES.MODE_ECB)

    def encrypt(self, data: str) -> str | None:
        try:
            encrypt_data = self.cipher.encrypt(
                pad(data.encode("utf-8"), AES.block_size)
            )
            return base64.b64encode(encrypt_data).decode("utf-8")
        except Exception as e:
            return None

    def decrypt(self, data: str) -> str | None:
        try:
            byte_data = base64.b64decode(data.encode("utf-8"))
            decrypt_data = unpad(self.cipher.decrypt(byte_data), AES.block_size)
            return decrypt_data.decode("utf-8")
        except Exception as e:
            return None
