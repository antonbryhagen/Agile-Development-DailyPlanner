"""Testing Activities."""
import unittest
from planner.Activities import Activities


class TestActivities(unittest.TestCase):
    """Testing class for Activities."""

    def test_init(self):
        """Init user test."""
        res = Activities("Test activity", "Important", "1", "TestUser")
        exp = Activities
        self.assertIsInstance(res, exp)
    

if __name__ == "__main__":
    unittest.main()
