import mysql.connector
import os

class DB_Handler:
    def __init__(self):
        self.host = "localhost"
        self.user = os.environ['MYSQL_USER']
        self.password = os.environ['MYSQL_PASSWORD']
        self.database = "DailyPlanner"
        self.connection = None
    
    def connect(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )

    def close(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.commit()
            self.connection.close()
    
    def query(self, query, values = None):
        cursor = self.connection.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        
        result = cursor.fetchall()
        cursor.close()
        return result