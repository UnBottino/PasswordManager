import security
import menu
import connection
import colorama

colorama.init()

encryption_key = security.login()

while True:
    choice = menu.main_menu()

    if choice.casefold() == '1':
        #Create a password
        menu.create_pword_menu()
    elif choice.casefold() == '2':
        #Get all passwords
        connection.get_all()
    elif choice.casefold() == '3':
        #Search by site
        menu.get_by_site_menu()
    elif choice.casefold() == '4':
        #Delete a password
        menu.delete_pword_menu()
    elif choice.casefold() == '5':
        #Change master password
        security.change_master()
    elif choice.casefold() == 'Q'.casefold():
        menu.print_msg('Goodbye!', 'blue')
        print('-'*30)
        break
    else:
        menu.print_msg('Invalid option!', 'yellow')

exit()