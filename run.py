from credentials import Credentials
from user import User
import random


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


