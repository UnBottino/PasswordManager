# PasswordManager
A python program which allows a user to store their login details for accounts/sites.

# Getting Started
- Create a new Firestore project.
  - Insde this project create a new Firestore Database.
- Generate a private key file for your service account.
  - In the Firebase console, open Settings > Service Accounts.
  - Click Generate New Private Key, then confirm by clicking Generate Key.
  - Securely store the JSON file containing the key.
- Open "connection.py" and insert the path to the JSON file on line 11.

## Prerequisites
The following python packages are required
- firebase_admin
- termcolor
- cryptography
- bcrypt

An installation example would be:
- Open a command prompt and enter
```
py -m pip install firebase_admin
```
