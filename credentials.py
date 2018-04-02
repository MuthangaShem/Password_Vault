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

