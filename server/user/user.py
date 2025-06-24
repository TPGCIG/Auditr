class User:
    def __init__(self, user_id: int, name: str):
        self._user_id = user_id
        self._name = name
        self._graded_work = []

    def add_graded_work(self, graded_work):
        self._graded_work.append(graded_work)

    def get_all_graded_work(self):
        return self._graded_work