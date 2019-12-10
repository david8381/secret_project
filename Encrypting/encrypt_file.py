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


if __name__ == '__main__':
    while True:
        encrypt_or_decrypt = input("0> Quit\n1> Encrypt a file\n2> Decrypt a file\n> ")
        if encrypt_or_decrypt == '0':
            exit()
        elif encrypt_or_decrypt == '1':
            encrypt_file(input("File path> "), input("Password> "))
        else:
            decrypt_file(input("File path> "), input("Password> "))
