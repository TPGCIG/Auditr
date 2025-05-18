from user import User


class UserManager:
    def __init__(self):
        self._users = {}

    def add_user(self, user: User):
        self._users[user._user_id] = user

    def get_user(self, user_id: int) -> User:
        return self._users.get(user_id)
    
    def get_users(self) -> dict[User]:
        return self._users