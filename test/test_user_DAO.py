import unittest
from unittest.mock import MagicMock, patch
from planner.user_DAO import user_DAO
from planner.user import User
from planner.Activities import Activities


class Test_user_DAO(unittest.TestCase):
    """Testing class for user_DAO"""

    def test_init(self):
        """Init user_DAO test."""
        test_user_DAO = user_DAO()
        host = test_user_DAO.host
        database = test_user_DAO.database
        connection = test_user_DAO.connection
        res = [host, database, connection]
        exp = ["localhost", "DailyPlanner", None]
        self.assertEqual(res, exp)

    def test_connect(self):
        """Testing if connected to database."""
        connector = user_DAO()
        connector.connect()
        res = connector.connection
        exp = None
        self.assertNotEqual(res, exp)

    def test_close(self):
        """Testing if disconnected from database."""
        connector = user_DAO()
        connector.connect()
        connector.close()
        res = connector.connection
        exp = connector.connection.is_connected()
        self.assertNotEqual(res, exp)

    def test_create_user(self):
        """Testing create_user method."""
        test_user_DAO = user_DAO()
        test_user = User("Test", "Test", "123")
        try:
            res = test_user_DAO.get_user_by_username("Test", "123")
            test_user_DAO.connect()
            cursor = test_user_DAO.connection.cursor()
            delete_user_query = "DELETE FROM users WHERE username = %s"
            delete_user_values = ("Test",)
            cursor.execute(delete_user_query, delete_user_values)
            test_user_DAO.close()
            cursor.close()
            test_user_DAO.create_user(test_user)
        except Exception:
            test_user_DAO.create_user(test_user)
        finally:
            res = test_user_DAO.get_user_by_username("Test", "123")
            exp = "Test"
            self.assertEqual(res[0], exp)

    def test_get_user_by_username(self):
        """Testing get_user_by_username method."""
        test_user_DAO = user_DAO()
        try:
            user = test_user_DAO.get_user_by_username("Test", "123")
        except Exception:
            test_user = User("Test", "Test", "123")
            test_user_DAO.create_user(test_user)
        finally:
            res = test_user_DAO.get_user_by_username("Test", "123")
            exp = "Test"
            self.assertEqual(res[0], exp)
      
    def test_create_activity(self):
        """Test create_activity method."""
        mock_cursor = MagicMock()
        mock_cursor.execute.return_value = "execute"
        self.test_user_DAO = user_DAO()
        self.test_user_DAO.cursor = mock_cursor
        test_activity = Activities("TestActivity", "Important", "2", "Test")
        self.test_user_DAO.create_activity(test_activity)
        self.assertEqual(("TestActivity", "Important", "2", "Test",), self.test_user_DAO.create_activity_values)
        self.assertEqual(mock_cursor.execute(), "execute")
        mock_cursor.execute.assert_called_once()
    
    def test_delete_activity(self):
        "Test delete_activity method."
        mock_cursor = MagicMock()
        mock_cursor.execute.return_value = "execute"
        self.test_user_DAO = user_DAO()
        self.test_user_DAO.cursor = mock_cursor
        mock_user = User('test', 'test', 'test')
        test_activity = Activities("TestActivity", "Important", "2", "Test")
        self.test_user_DAO.delete_activity(test_activity, mock_user)
        self.assertEqual(self.test_user_DAO.list, ["TestActivity", 'test'])
        self.assertEqual(mock_cursor.execute(), "execute")
        mock_cursor.execute.assert_called_once()


if __name__ == "__main__":
    unittest.main()
