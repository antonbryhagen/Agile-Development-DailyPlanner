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

    @patch('planner.schedule_DAO.Schedule_DAO.connect')
    def test_create_schedule(self, mock_connect):
        schedule = {('test', 'Very important', 1, '')}
        test_object = schedule_DAO.Schedule_DAO()
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        test_object.connection = mock_connection
        test_object.connection.cursor = mock_cursor
        test_object.create_schedule(schedule, 'test')
        mock_connect.assert_called_once()
    
    @patch('planner.schedule_DAO.Schedule_DAO.connect')
    def test_delete_schedule(self, mock_connect):
        test_object = schedule_DAO.Schedule_DAO()
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        test_object.connection = mock_connection
        test_object.connection.cursor = mock_cursor
        test_object.delete_schedule('test')
        mock_connect.assert_called_once()
    
    @patch('planner.schedule_DAO.Schedule_DAO.connect')
    def test_get_schedule(self, mock_connect):
        test_object = schedule_DAO.Schedule_DAO()
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        test_object.connection = mock_connection
        test_object.connection.cursor = mock_cursor
        result = test_object.get_schedule('test')
        self.assertNotEqual(None, result)



if __name__ == "__main__":
    unittest.main()
