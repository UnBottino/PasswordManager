import os
from cryptography.fernet import Fernet
import connection
import menu

#Current directory
dir_path = os.path.dirname(os.path.realpath(__file__))

class Encryptor():
    def key_create():
        key = Fernet.generate_key()
        Encryptor.key_save(key)
        connection.store_encryption(key)
        return key

    def key_save(key):
        with open(dir_path + '/mykey.key', 'wb') as mykey:
            mykey.write(key)

    def key_load():
        try:
            with open(dir_path + '/mykey.key', 'rb') as mykey:
                return mykey.read()
        except:
            menu.print_msg('mykey.key file not found!', 'yellow')
            return None

    def pword_encrypt(key, original_pword):
        f = Fernet(key)
        return f.encrypt(original_pword.encode('utf-8'))

    def pword_decrypt(key, encrypted_pword):
        f = Fernet(key)
        return f.decrypt(encrypted_pword)