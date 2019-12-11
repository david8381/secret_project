import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def generate_key(password_provided):
    password = password_provided.encode() # Convert to type bytes
    salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once


def encrypt(text, password):
    text = text.encode()
    f = Fernet(generate_key(password))
    encrypted = f.encrypt(text)
    return encrypted.decode()


def decrypt(encrypted_text, password):
    f = Fernet(generate_key(password))
    to_decrypt = encrypted_text.encode()
    decrypted = f.decrypt(to_decrypt)
    return decrypted.decode()


if __name__ == '__main__':
    password = input("Password> ")
    text = input("Text to encrypt> ")
    key = generate_key(password) # This line is not needed. Just so it can be printed later so the user can see the key

    encrypted_text = encrypt(text, password)
    decrypted_text = decrypt(encrypted_text, password)

    print("\n\n")
    print("Password: " + password)
    print("Key from password: " + key.decode())
    print("\nText you entered:\n" + text)
    print("\nEncrypted text:\n" + encrypted_text.decode())
    print("\nAfter decrypting encrypted text:\n" + decrypted_text.decode())
    print("\n")
    print("text == decrypted_text: " + str(str(text) == str(decrypted_text.decode())))
    print("\n\n")
