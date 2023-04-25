# Installation Guide

## Install MySQL:

1. Download and install MySQL Installer from [https://dev.mysql.com/downloads/](https://dev.mysql.com/downloads/).
2. Follow the installation instructions based on your operating system.
3. In MySQL Workbench, open the localhost instance
4. From the instance menu to the left, click Startup/Shutdown and start MySQL Server


## Set Local Variables:

1. Create a virtual environment and activate it using Git Bash in the project directory.
2. Set the local variables for the MySQL username and password using the following commands:
    - On Windows: `set MYSQL_USER=username` and `set MYSQL_PASSWORD=password`
    - On Mac/Linux: `export MYSQL_USER=username` and `export MYSQL_PASSWORD=password`

## Enable PowerShell Scripts to Run:

1. Open PowerShell as an administrator.
2. Run the following command to enable script execution: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`

## Create the Database:

1. Run the following script using Git Bash: `python db/db_init.py`
2. This will create the 'DailyPlanner' database in MySQL.
