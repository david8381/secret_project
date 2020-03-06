import encrypt as e

def encrypt_file(file_path, password):
    f = open(file_path, 'r')
    contents = f.read()
    encrypted = e.encrypt(contents, password)
    f.close()
    f = open(file_path, 'w')
    f.write(encrypted)
    f.close()


def decrypt_file(file_path, password):
    f = open(file_path, 'r')
    contents = f.read()
    decrypted = e.decrypt(contents, password)
    f.close()
    f = open(file_path, 'w')
    f.write(decrypted)
    f.close


def encrypt_text(text, password):
    encrypted = e.encrypt(text, password)
    return encrypted

def decrypt_text(text, password):
    decrypted = e.decrypt(text, password)
    return decrypted


if __name__ == '__main__':
    while True:
        encrypt_or_decrypt = input("0> Quit\n1> Encrypt a file\n2> Decrypt a file\n3> Encrypt text\n4> Decrypt text\n")
        if encrypt_or_decrypt == '0':
            exit()
        elif encrypt_or_decrypt == '1':
            encrypt_file(input("File path> "), input("Password> "))
        elif encrypt_or_decrypt == '2':
            decrypt_file(input("File path> "), input("Password> "))
        elif encrypt_or_decrypt == '3':
            print(encrypt_text(input("Text>\n"), input("Password> ")))
        else:
            print(decrypt_text(input("Text>\n"), input("Password> ")))
