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
    
    def create_schedule(self, schedule):
        """Create new schedule in database using schedule object."""
        self.connect()
        cursor = self.connection.cursor()
        create_schedule_query = (
            "INSERT INTO schedules () VALUES(%s, %s, %s)"
        )
        create_schedule_values = (schedule.username, schedule.name, schedule.password)
        cursor.execute(create_schedule_query, create_schedule_values)
        self.close()
        cursor.close()
    
    def delete_schedule(self):
        pass
    
    def get_schedule(self):
        pass 