"""Handle db access for users and activities."""

import os
import mysql.connector
import bcrypt


class user_DAO:
    """Class for accessing user database."""

    def __init__(self):
        """Create instance attributes for database connection."""
        self.host = "localhost"
        self.user = os.environ["MYSQL_USER"]
        self.password = os.environ["MYSQL_PASSWORD"]
        self.database = "DailyPlanner"
        self.connection = None

    def connect(self):
        """Connect to database using instance attributes."""
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
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
        create_user_query = (
            "INSERT INTO users (username, name, password) VALUES(%s, %s, %s)"
        )
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
        if user_data is not None:
            hashed_password = user_data[2]
        else:
            return False
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8")):
            print("Valid login information")
            return [user_data[0], user_data[1]]
        else:
            print("Invalid login information")
            return False

    def create_activity(self, activity):
        """Create new activity in database using activity object."""
        self.connect()
        self.cursor = self.connection.cursor()
        create_activity_query = ("INSERT INTO activities "
                                 "(Activity, PRIO, Time, username) VALUES(%s, %s, %s, %s)")
        self.create_activity_values = (
            activity.Activity,
            activity.PRIO,
            activity.Time,
            activity.username,
        )
        self.cursor.execute(create_activity_query, self.create_activity_values)
        self.close()
        self.cursor.close()

    def get_activities(self, user):
        """Get all activities stored for a specific user."""
        self.connect()
        cursor = self.connection.cursor()
        get_activities_query = ("SELECT Activity, PRIO, Time, idActivity "
                                "FROM activities where username = %s")
        get_activities_values = (user.username,)
        cursor.execute(get_activities_query, get_activities_values)
        actvities_data = cursor.fetchall()
        self.close()
        cursor.close()
        return actvities_data

    def delete_activity(self, activity, user_object):
        """Delete activity in database using activity object."""
        self.connect()
        self.cursor = self.connection.cursor()
        self.activity = activity.Activity
        self.current_username = user_object.username
        self.list = []
        self.list.append(self.activity)
        self.list.append(self.current_username)
        delete_activity_query = ("DELETE FROM activities "
                                 "WHERE Activity = %s AND username = %s LIMIT 1;")
        delete_activity_values = self.list
        self.cursor.execute(delete_activity_query, delete_activity_values)
        self.close()
        self.cursor.close()
