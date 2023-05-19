import mysql.connector
import os

class Schedule_DAO:
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
    
    def create_schedule(self, schedule_list, username):
        """Create new schedule in database using schedule object."""
        #username idActivity
        self.connect()
        cursor = self.connection.cursor()
        create_schedule_query = (
            "INSERT INTO schedules (username, idActivity) VALUES(%s, %s)"
        )
        for activity in schedule_list:
            create_schedule_values = (username, activity[3])
            cursor.execute(create_schedule_query, create_schedule_values)
        self.close()
        cursor.close()
    
    def delete_schedule(self, username):
        """Delete schedule for specified user."""
        self.connect()
        cursor = self.connection.cursor()
        delete_schedule_query = (
            "DELETE FROM schedules WHERE username = %s"
        )
        delete_schedule_values = (username,)
        cursor.execute(delete_schedule_query, delete_schedule_values)
        self.close()
        cursor.close()
    
    def get_schedule(self, username):
        """Return list of activites sorted as schedule."""
        self.connect()
        cursor = self.connection.cursor()
        get_schedule_query = (
            "SELECT username, idActivity, scheduleID FROM schedules WHERE username = %s"
        )
        get_schedule_values = (username,)
        cursor.execute(get_schedule_query, get_schedule_values)
        schedule_list = cursor.fetchall()
        self.close()
        cursor.close()
        return schedule_list