import bcrypt

class User:
    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.password = self.hash_password(password)
    
    def hash_password(password):
        password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password, salt)
        return hashed_password