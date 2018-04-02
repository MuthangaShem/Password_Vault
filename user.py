class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = []  # Empty contact list

    def __init__(self, first_name, last_name, login_password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.login_password = login_password
