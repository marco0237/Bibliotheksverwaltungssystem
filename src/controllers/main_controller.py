
from models.user_model import UserModel


class MainController:

    def __init__(self, model: UserModel) -> None:
        self.model = model

    def save(self, email):
        self.model.save()
