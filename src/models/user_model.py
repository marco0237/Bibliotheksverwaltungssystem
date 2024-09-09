

class UserModel:
    def __init__(self, username="", email=""):
        self.username = username
        self.email = email

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
