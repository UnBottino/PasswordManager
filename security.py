import os
import bcrypt
import encryptor as crypt
import menu
import connection

#Current directory
dir_path = os.path.dirname(os.path.realpath(__file__))

def login():
    secret = secret_load()

    if not connection.check_for_encryption():
        encryption_key = crypt.Encryptor.key_create()

    while True:
        menu.print_msg('Enter master password to start:', 'blue')
        passw = input()
        
        if check_master_pword(passw, secret):
            break

        menu.print_msg('Wrong password!', 'yellow')
        continue

    encryption_key = crypt.Encryptor.key_load()

    if encryption_key is None:
        encryption_key = connection.get_encryption()
        crypt.Encryptor.key_save(encryption_key)
        menu.print_msg('mykey.key restored', 'green')
        return encryption_key
    else:
        return encryption_key

def change_master():
    secret = secret_load()
    old_master = menu.request_master()
    if check_master_pword(old_master, secret):
        new_master =  menu.change_master_menu()
        while True:
            menu.print_msg('Are you sure you want to continue? (Y/N)', 'blue')
            choice = input(':')

            if choice.casefold() not in ('y', 'n'):
                print('Invalid option')
                continue
            else:
                if choice.casefold() == 'y':
                    new_secret = pword_hash(new_master)
                    secret_save(new_secret)
                    connection.update_secret(new_secret)
                    menu.print_msg('Master password has been updated!', 'green')
                else:
                    menu.print_msg('Exiting master password change!', 'yellow')
            break
    else:
        menu.print_msg('Incorect Password!', 'yellow')
        return

def create_master_pword():
    master_pword =  menu.create_master_menu()   
    secret = pword_hash(master_pword)
    secret_save(secret)
    connection.store_secret(secret)
    return secret

def secret_save(secret):
    with open(dir_path + '/secret.txt', 'wb') as mySecret:
        mySecret.write(secret)

def secret_load():
    try:
        with open(dir_path + '/secret.txt', 'rb') as mySecret:
            return mySecret.read()
    except:
        menu.print_msg('secret.txt file not found!', 'yellow')

        if connection.check_for_secret():
            secret = connection.get_secret()
            secret_save(secret)
            menu.print_msg('Secret restored', 'green')
        else:
            secret = create_master_pword()
        
        return secret

def check_master_pword(input_pass, secret):
    return bcrypt.checkpw(input_pass.encode('utf-8'), secret) 

def pword_hash(pword):
    bytePwd = pword.encode('utf-8')
    mySalt = bcrypt.gensalt()
    return bcrypt.hashpw(bytePwd, mySalt)