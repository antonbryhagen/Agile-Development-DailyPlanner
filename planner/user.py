import bcrypt

class User:
    """Create user object and hash the password."""
    def __init__(self, username, name, password):
        """Create instance attributes and call hash method."""
        self.username = username
        self.name = name
        self.password = self.hash_password(password)
    
    def hash_password(self, password):
        """Hash the password using bcrypt."""
        password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password, salt)
        return hashed_password