class User:
    """
    Class that generates new instances of users.
    """

    user_list = []  # Empty contact list

    def __init__(self, first_name, last_name, email, login_password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_password = login_password

    def save_user(self):
        """
        save_user method saves user objects into user_list

        """

        User.user_list.append(self)
