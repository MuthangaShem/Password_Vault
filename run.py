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


def find_existing_credentials(website):
    '''
        Function that check if a credential exists with that website and return a Boolean
        '''
    return Credentials.credentials_exist(website)


def display_credentials():
    '''
        Function that returns all the saved credentials
        '''
    return Credentials.display_credentials()


def main():
    print("Hello and welcome to your Passwords Vault. An app that help you generate and/or store passwords for your numerous accounts")
    print('\n')


if __name__ == '__main__':
    main()
