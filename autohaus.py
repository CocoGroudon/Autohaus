from credentialManager import CredentialManager

class Autohaus:
    def __init__(self):
        self.credentialManager = CredentialManager()
        self.user = None    
    
    def set_user(self, user):
        self.user = user

    def logout(self):
        self.user = None