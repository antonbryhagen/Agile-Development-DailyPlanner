"""Feature tests for planner"""
import unittest
from unittest.mock import patch, Mock

from planner import user_dao
from planner import user
from planner import activities



class TestMain(unittest.TestCase):
    """Class for testing main."""

    def test_create_user_and_log_in(self):
        """Test for creating a user and use it to login."""
        
        # Create user object as if using register form
        # TODO Check if the following user exists, if it does, delete it
        # before creating a new 
        self.user_username = "TestFeatureUser"
        self.user_name = "FeatureUser"
        self.user_password = "FeaturePass"
        
        self.user_DAO_handler = user_dao.UserDAO()
        
        self.user_object = user.User(
            self.user_username, self.user_name, self.user_password
        )
        try:
            self.user_DAO_handler.connect()
            cursor = self.user_DAO_handler.connection.cursor()
            delete_user_query = "DELETE FROM users WHERE username = %s"
            delete_user_values = ("TestFeatureUser",)
            cursor.execute(delete_user_query, delete_user_values)
            self.user_DAO_handler.close()
            cursor.close()
        except:
            pass
        finally:
            self.user_DAO_handler.create_user(self.user_object)
        
        
        # Test log in using above user as if using login form
        
        self.stored_username, self.stored_name = self.user_DAO_handler.get_user_by_username("TestFeatureUser", "FeaturePass")
        self.assertEqual(self.stored_name, "FeatureUser")
        
                


if __name__ == "__main__":
    unittest.main()
