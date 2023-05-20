"""Testing Activities."""
import unittest
from planner import activities


class TestActivities(unittest.TestCase):
    """Testing class for Activities."""

    def test_init(self):
        """Init user test."""
        res = activities.Activities("Test activity", "Important", "1", "TestUser")
        exp = activities.Activities
        self.assertIsInstance(res, exp)
    

if __name__ == "__main__":
    unittest.main()
