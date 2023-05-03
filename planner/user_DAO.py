import mysql.connector
import os
import bcrypt


class user_DAO:
    """Class for accessing user database."""
    def __init__(self):
        """Create instance attributes for database connection."""
        self.host = "localhost"
        self.user = os.environ['MYSQL_USER']
        self.password = os.environ['MYSQL_PASSWORD']
        self.database = "DailyPlanner"
        self.connection = None
    
    def connect(self):
        """Connect to database using instance attributes."""
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )

    def close(self):
        """Commit any changes to database and close connection to database."""
        if self.connection is not None and self.connection.is_connected():
            self.connection.commit()
            self.connection.close()
    
    def create_user(self, user):
        """Create new user in database using user object."""
        self.connect()
        cursor = self.connection.cursor()
        create_user_query = ("INSERT INTO users (username, name, password) VALUES(%s, %s, %s)")
        create_user_values = (user.username, user.name, user.password)
        cursor.execute(create_user_query, create_user_values)
        self.close()
        cursor.close()

    def get_user_by_username(self, username, password):
        """Get user from database using username and matching password."""
        self.connect()
        cursor = self.connection.cursor()
        get_user_query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(get_user_query, (username,))
        user_data = cursor.fetchone()
        hashed_password = user_data[2]
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            print("Valid login information")
            return [user_data[0], user_data[1]]
        else:
            print("Invalid login information")
            return False

        
    def create_activity(self, activity):
        """Create new activity in database using activity object."""
        self.connect()
        cursor = self.connection.cursor()
        create_activity_query = ("INSERT INTO activities (Activity, PRIO, Time, username) VALUES(%s, %s, %s, %s)")
        create_activity_values = (activity.Activity, activity.PRIO, activity.Time, activity.username)
        cursor.execute(create_activity_query, create_activity_values)
        self.close()
        cursor.close()
        
        
    def delete_activity(self, activity):
        """Delete activity in database using activity object."""
        self.connect()
        cursor = self.connection.cursor()
        activity = activity.Activity
        list = []
        list.append(activity)
        create_activity_query = ("DELETE FROM activities WHERE Activity = %s  LIMIT 1; VALUES(%s)")
        create_activity_values = (list)
        cursor.execute(create_activity_query, create_activity_values)
        self.close()
        cursor.close()