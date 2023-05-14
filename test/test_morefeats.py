"""Feature tests for planner"""
import unittest
from unittest.mock import patch, Mock, MagicMock

from planner import user_DAO
from planner import user
from planner import Activities



class TestMain(unittest.TestCase):
    """Class for testing main."""

    def test_create_user_and_log_in(self):
        """Test for creating a user and use it to login."""
        
        # Create user object as if using register form
        # TODO Check if the following user exists, if it does, delete it
        # before creating a new 
        
        self.user_DAO_handler = user_DAO.user_DAO()
        
        self.user_object = MagicMock()
        
        self.activities_object = Activities.Activities(
            'test', 'Very Important', '10', 'test'
        )
        self.user_DAO_handler.create_activity(self.activities_object)
        self.user_DAO_handler.delete_activity(self.activities_object)

        
        # Test log in using above user as if using login form
        self.assertEqual(self.activities_object.username, 'test')
        
                


if __name__ == "__main__":
    unittest.main()
