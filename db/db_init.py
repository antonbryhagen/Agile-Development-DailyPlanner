import mysql.connector
import os

# Get variables from OS

os_username = os.environ.get('MYSQL_USER')
os_password = os.environ.get('MYSQL_PASSWORD')


# Connect to the MySQL server
db = mysql.connector.connect(
  host = "localhost",
  user = os_username,
  password = os_password
)

# Create a new database called DailyPlanner
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS DailyPlanner")

# Connect to the DailyPlanner database
db = mysql.connector.connect(
  host = "localhost",
  user = os_username,
  password = os_password,
  database = "DailyPlanner"
)

# Create a table called users with columns for username, name, and password
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(255) PRIMARY KEY, name VARCHAR(255), password VARCHAR(255))")
cursor.execute("CREATE TABLE IF NOT EXISTS activities (idActivity INT PRIMARY KEY NOT NULL AUTO_INCREMENT,PRIO VARCHAR(255), Activity VARCHAR(255), Time INT, username VARCHAR(255) REFERENCES users(username))")
cursor.execute("CREATE TABLE IF NOT EXISTS schedules (scheduleID INT PRIMARY KEY NOT NULL AUTO_INCREMENT, username VARCHAR(255) REFERENCES users(username), idActivity INT REFERENCES activities(idActivity))")
