"""Testing user."""
import unittest
from planner.user import User


class TestUser(unittest.TestCase):
    """Testing class for user."""

    def test_init(self):
        """Init user test."""
        res = User("username", "name", "password")
        exp = User
        self.assertIsInstance(res, exp)

    def test_hash_password(self):
        """Testing the hash password method."""
        testUser = User("username", "name", "password")
        res = testUser.password
        exp = "password"
        self.assertNotEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
