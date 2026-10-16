class LoginService:
    def __init__(self):
        self.users = {"admin": "admin123", "etudiant": "ensa2026"}

    def validate(self, username, password):
        if not username or not password:
            raise ValueError("Identifiant et mot de passe obligatoires")
        if len(password) < 6:
            raise ValueError("Mot de passe trop court (6 caracteres minimum)")

    def login(self, username, password):
        self.validate(username, password)
        if username not in self.users:
            raise ValueError("Utilisateur inconnu")
        return self.users[username] == password