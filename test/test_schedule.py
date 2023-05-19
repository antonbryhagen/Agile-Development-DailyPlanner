import unittest
from unittest.mock import MagicMock, patch, call, ANY
from planner import schedule


class TestSchedule(unittest.TestCase):

    def test_init(self):
        mock_activities = MagicMock()
        test_object = schedule.Schedule(mock_activities, '10')
        self.assertEqual(test_object.time_per_day['Monday'], '10')
        self.assertEqual(test_object.time_per_day['Tuesday'], '10')
        self.assertEqual(test_object.time_per_day['Wednesday'], '10')
        self.assertEqual(test_object.time_per_day['Thursday'], '10')
        self.assertEqual(test_object.time_per_day['Friday'], '10')

    def test_sort_activities(self):
        mock_activities = MagicMock()
        test_object = schedule.Schedule(mock_activities, '10')
        test_object.sort_activities()
        self.assertIsInstance(test_object.activities, list)

    @patch('planner.schedule.Schedule.sort_activities')
    def test_generate_schedule(self, mock_sort):
        mock_sort.return_value = MagicMock()
        mock_activities = MagicMock()
        test_object = schedule.Schedule(mock_activities, '10')
        test_object.generate_schedule(1, 1)
        self.assertIsInstance(test_object.days, dict)


    def test_generate_schedule_with_lunch(self):
        self.schedule_generator.generate_schedule(7, 1)
        self.assertIn(('Lunch', 'Very important', 1, ''), self.schedule_generator.days['Monday'])
        self.assertNotIn(('Lunch', 'Very important', 1, ''), self.schedule_generator.days['Tuesday'])
        # ... assert other days and activities

if __name__ == "__main__":
    unittest.main()
