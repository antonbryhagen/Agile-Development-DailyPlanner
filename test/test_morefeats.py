"""Feature tests for planner"""
import unittest
from unittest.mock import patch, Mock, MagicMock

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
        
        self.user_DAO_handler = user_dao.UserDAO()
        
        self.user_object = user.User('test', 'test', 'test')
        
        self.activities_object = activities.Activities(
            'test', 'Very Important', '10', 'test'
        )
        self.user_DAO_handler.create_activity(self.activities_object)
        self.user_DAO_handler.delete_activity(self.activities_object, self.user_object)

        
        # Test log in using above user as if using login form
        self.assertEqual(self.activities_object.username, 'test')
        
                


if __name__ == "__main__":
    unittest.main()
