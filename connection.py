import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from account import Account
import encryptor as crypt
import menu

#=====================
#Fill in your own path
#=====================
cred = credentials.Certificate('path/to/serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

#Firestore collection names
firestore_accounts = db.collection('accounts')
firestore_encryption = db.collection('encryption_key')
firestore_secret = db.collection('secret')

def check_for_encryption():
    if firestore_encryption.get():
        return True
    else:
        return False 

def store_encryption(encryption_key):
    firestore_encryption.document().set({u'key': encryption_key})

def get_encryption():
    doc_list = firestore_encryption.get()
    return doc_list[0].get(u'key')

def check_for_secret():
    if firestore_secret.get():
        return True
    else:
        return False 

def store_secret(secret):
    firestore_secret.document().set({u'secret': secret})

def get_secret():
    doc_list = firestore_secret.get()
    return doc_list[0].get(u'secret')

def update_secret(new_secret):
    doc_list = firestore_secret.get()
    doc_list[0].reference.update({u'secret': new_secret})


def add_pword(site, username, pword):
    pword_exists = check_for_dup(site.lower(), username.lower())

    if pword_exists:
        menu.print_msg('Password already stored!', 'yellow')
    else:
        encryption_key = crypt.Encryptor.key_load()
        encrypted = crypt.Encryptor.pword_encrypt(encryption_key, pword)

        firestore_accounts.document().set({
            u'site': site,
            u'site_insensitive': site.lower(),
            u'username': username,
            u'username_insensitive': username.lower(),
            u'password': encrypted      
        })

        menu.print_msg('Password saved!', 'green')

def get_all():
    doc_list = firestore_accounts.get()

    if not doc_list:
        menu.print_msg('No passwords found!', 'yellow')
    else:
        encryption_key = crypt.Encryptor.key_load()

        for doc in doc_list:
            decrypted_pword = crypt.Encryptor.pword_decrypt(encryption_key, doc.get('password'))
            acc = Account(doc.get(u'username'), decrypted_pword.decode('utf-8'), doc.get('site'))
            Account.show(acc)

def get_by_site(input_site_insensitive):
    doc_list = firestore_accounts.where(u'site_insensitive', u'>=', input_site_insensitive).where(u'site_insensitive', u'<=', input_site_insensitive + '\uf8ff').get()

    if not doc_list:
        menu.print_msg('No passwords found!', 'yellow')
    else:
        encryption_key = crypt.Encryptor.key_load()

        for doc in doc_list:
            decrypted_pword = crypt.Encryptor.pword_decrypt(encryption_key, doc.get(u'password'))
            acc = Account(doc.get(u'username'), decrypted_pword.decode('utf-8'), doc.get('site'))
            Account.show(acc)

def delete_pword(site, username):
    pword_exists = check_for_dup(site, username)
    if pword_exists:
        if menu.delete_confirm_menu(site, username):
            doc = get_account(site, username)

            doc.reference.delete()
            menu.print_msg('Password deleted!', 'green')
        else:
            menu.print_msg('Password delete canceled!', 'yellow')
    else:
        menu.print_msg('No password found!', 'yellow')

def get_account(site, username):
    doc_list = firestore_accounts.where(u'site_insensitive', u'==', site.lower()).where(u'username_insensitive', u'==', username.lower()).get()

    if not doc_list:
        return None
    else:
        return doc_list[0]

def check_for_dup(site, username):
    doc = get_account(site, username)

    if not doc:
        return False
    else:
        return True