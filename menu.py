from termcolor import colored
import connection

def create_master_menu():
    print_msg('Create a master password', 'blue')
    return input(':')

def request_master():
    print_msg('Please enter your current master password to continue', 'blue')
    return input(':')

def change_master_menu():
    while True:
        print_msg('Please enter your new master password', 'blue')
        new_master =  input(':')
        print_msg('Re-enter your new master password', 'blue')
        new_master_match =  input(':')

        if new_master == new_master_match:
            return new_master
        else:
            print_msg('Passwords dont match!', 'yellow')
            continue

def main_menu():
    print('-'*30)
    print(('-'*13) + 'Menu' + ('-'*13))
    print('1. Create a new password')
    print('2. Find all passwords')
    print('3. Find a password by site name')
    print('4. Delete a password')
    print('5. Change master password')
    print('Q. Exit')
    print('-'*30)
    return input(': ')

def create_pword_menu():
    print_msg('Enter site name', 'blue')
    site = input(': ')
    print_msg('Enter username', 'blue')
    username = input(': ')
    print_msg('Enter password', 'blue')
    pword = input(': ')
    connection.add_pword(site, username, pword)

def get_by_site_menu():
    print_msg('Please enter the site name', 'blue')
    input_site = input(': ')
    connection.get_by_site(input_site.lower())

def delete_pword_menu():
    print_msg('Enter Site name', 'blue')
    site = input(': ')
    print_msg('Enter username', 'blue')
    username = input(': ')
    connection.delete_pword(site, username)

def delete_confirm_menu(site, username):
    while True:
        print_msg('Are you sure you want to delete the information for "{}" on "{}"? (Y/N)'.format(username, site), 'blue')
        answer = input(':')

        if answer.casefold() == 'y':
            return True
        elif answer.casefold() == 'n':
            return False
        else:
            print_msg('Invalid input!', 'yellow')
            continue


def print_msg(text, color):
    print('-'*30)
    print(colored(text, color, attrs=['bold']))