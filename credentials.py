class Credentials:
    """
    class that generates new instances of credentials
    """
    credentials_list = []  # empty credentials list

    def __init__(self, website, username, password):
        """
        _init_ method that helps us define properties of our objects

        Args:
        website: new credential website
        username: new credential username in that website
        password: new credential password in that website
        """
        self.website = website
        self.username = username
        self.password = password

    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_website(cls, website):
        '''
        Method that takes in a website and returns a credentials that matches that website.

        Args:
            website: website to search for
        Returns :
            credentials that matches the website.
        '''
        for credentials in cls.credentials_list:
            if credentials.website == website:
                return credentials

    @classmethod
    def credentials_exist(cls, website):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            website: website to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for credentials in cls.credentials_list:
            if credentials.website == website:
                return True

        return False
