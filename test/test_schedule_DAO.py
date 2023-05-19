import unittest
from unittest.mock import MagicMock, patch, call, ANY
from planner import schedule_DAO


class TestSchedule_DAO(unittest.TestCase):

    def test_init(self):
        test_object = schedule_DAO.Schedule_DAO()
        self.assertEqual(test_object.host, 'localhost')
        self.assertEqual(test_object.database, 'DailyPlanner')

    def test_connect(self):
        test_object = schedule_DAO.Schedule_DAO()
        test_object.connect()
        exp = None
        self.assertNotEqual(test_object.connection, exp)

    def test_close(self):
        test_object = schedule_DAO.Schedule_DAO()
        test_object.connect()
        test_object.close()
        exp = test_object.connection.is_connected()
        self.assertNotEqual(test_object.connection, exp)

    def test_create_schedule(self):
        mock_schedule = MagicMock()


    def test_shuffle(self):
        mock_shuffle_schedule = MagicMock()

if __name__ == "__main__":
    unittest.main()
