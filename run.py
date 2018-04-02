from credentials import Credentials
from user import User
import random

def create_credentials(website, username, password):
	'''
    Function to create a new credentials
    '''
    new_credentials = Credentials(website, username, password)
    return new_credentials