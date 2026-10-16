class LoginService:
    def __init__(self):
        self.users = {"admin": "admin123", "etudiant": "ensa2026"}

    def login(self, username, password):
        return self.users.get(username) == password