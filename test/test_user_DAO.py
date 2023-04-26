import unittest
import mysql.connector
from planner.user_DAO import user_DAO

class Test_user_DAO(unittest.TestCase):
    """Testing class for user_DAO"""
    
    def test_init(self):
        """Init user_DAO test."""
        mysql.connector.connect()

    def test_connect(self):
        """Testing if connected to database."""
        res = user_DAO.connect