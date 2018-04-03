from credentials import Credentials
from user import User
import random


def create_user(first_name, last_name, email, login_password):
    '''
Function to create a new user
'''
    new_user = User(first_name, last_name, email, login_password)
    return new_user


def save_user(user):
    '''
Function to save user
'''
    user.save_user


def create_credentials(website, username, password):
    '''
Function to create a new credentials
'''
    new_credentials = Credentials(website, username, password)
    return new_credentials


def save_credentials(credentials):
    '''
    function to save credentials
    '''
    credentials.save_credentials()


def delete_credentials(credentials):
    '''
        function to delete credentials
        '''
    return credentials.delete_credentials()


def find_credentials(website):
    '''
    function that finds credentials by website and returns the credentials
    '''
    return Credentials.find_by_website(website)


def check_existing_credentials(website):
    '''
        Function that check if a credential exists with that website and return a Boolean
        '''
    return Credentials.credentials_exist(website)


def display_credentials():
    '''
        Function that returns all the saved credentials
        '''
    return Credentials.display_credentials()


def generate_password(pass_length):
    '''
    function for generating password
    '''
    return Credentials.generate_password(pass_length)


def main():

    login = True

    while login:

        print('---' * 20)
        print("Hello and welcome to your Passwords Vault.")
        print('---' * 20)
        print('\n')

        print('Please enter your first name...')
        print()
        first_name = str(input())
        print('\n')

        print('Please enter your last name...')
        print()
        last_name = str(input())
        print('\n')

        print(f"Welcome {first_name} {last_name}." + "\n"
              + "Please choose a suitable login password...")
        print('\n')

        login_password = input()
        print('\n')

        print("please confirm the password by entering it again.")
        login_password_repeat = input()
        print('\n')

        if login_password == login_password_repeat:
            print()
            print("Registration successful!!")
            print('\n')

            execute = True
            while execute:
                print("-" * 10 + "Use these short codes :" + "-" * 10)
                print()
                print(
                    "cc - create a new credential, dc - display credential, fc -find a credential, ex -exit The Passwords Vault")
                print('----' * 20)
                short_code = input().lower()

                if short_code == 'cc':
                    print("New Credentials")
                    print('----' * 10)

                    print('Website...')
                    website = input()

                    print(f'Username you use for {website} ...')
                    username = input()

                    print("How long would you like your password to be?")
                    pass_length = int(input())
                    password = generate_password(pass_length)
                    print('----' * 10)
                    print("Your password is...")
                    print("---" * 10 + f"{password}" + "---" * 10)
                    print("Please do not share it with anyone")
                    print('----' * 10)
                    print()

                    save_credentials(create_credentials(
                        website, username, password))
                    print('\n')
                    print('----' * 10)
                    print("New Credentials created:" + "\n" +
                          f"website:  {website}" + "\n" +
                          f"username: {username}" + "\n" +
                          f"password: {password} ")
                    print('----' * 10)
                    print('\n')

                    execute = True

                elif short_code == 'dc':
                    if display_credentials():
                        print("Here's a lit of you credentials")
                        print('\n')
                        for credentials in display_credentials():
                            print('----' * 10)
                            print(f"Website:  {credentials.website}" + "\n" +
                                  f"Username: {credentials.username}" + "\n" +
                                  f"Password: {credentials.password}")
                            print('----' * 10)
                            print()
                            print()

                    else:
                        print()
                        print()
                        print(
                            "You don't seem to be having anything saved at the moment...")
                        print()
                        print()

                elif short_code == 'fc':
                    print("Please The website that you want to search for")
                    print()

                    search_website = input()
                    if check_existing_credentials(search_website):
                        search_credentials = find_credentials(search_website)
                        print('----' * 10)
                        print(f"Website: {search_credentials.website}" + '\n' +
                              f"Username: {search_credentials.username}" + '\n' +
                              f"Password: {search_credentials.password}")
                        print('----' * 10)

                    else:
                        print("Credentials for that website do not exist.")

                elif short_code == 'ex':
                    print("You are now login out. Good Bye...")
                    break

        if login_password != login_password_repeat:
            print()
            retry = input("Sorry... The passwords didn't match!!" + "\n" +
                          " Would you like to try again? (Y)es or (N)o?")
            if retry == "y".lower():
                login = True
            if retry == "n".lower():
                print("Thank you for your time. Good Bye")
                exit()


if __name__ == '__main__':
    main()
