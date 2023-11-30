from user import User

class CredentialManager:
    def __init__(self):
        self.credentials = {"admin": "admin",
                            "user": "user",
                            "coco": "coco"}

    def check_username(func):
        """Decorator to check if username is in credentials"""
        def wrapper(self, *args, **kwargs):
            if 'username' in kwargs and kwargs['username'] in self.credentials:
                return func(self, *args, **kwargs)
            else:
                return False
        return wrapper
    
    @check_username
    def validate_login(self, *,  username, password):
        if not self.credentials[username] == password:
            return False
        return True
    
    @check_username
    def get_user(self, *, username):
        return User(username=username, displayname=username)
    

