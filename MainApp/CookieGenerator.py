import base64
import random, string


def SecretKeyGenerator(length=10):
    characters = string.ascii_letters + string.digits
    key = ''.join(random.choice(characters) for _ in range(length))
    return key

class Cookie:
    def Generate(userName, userRole):
        new_key = SecretKeyGenerator() + ":" + userName + ":" + userRole + ":" + SecretKeyGenerator()
        enc_key = base64.b64encode(base64.b64encode(new_key.encode()))
        return enc_key.decode()

    def DecodeCookie(cookie_string):
        decoded_string = base64.b64decode(base64.b64decode(cookie_string.encode()))
        decoded_string = decoded_string.decode()

        decoded_string = decoded_string.split(':')
        return {
            'secretKey1': decoded_string[0],
            'username': decoded_string[1],
            'role': decoded_string[2],
            'secretKey2': decoded_string[3],
        }