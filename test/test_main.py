"""Testing main"""
import unittest
from unittest.mock import patch, Mock
from planner import main
from planner.interface import Interface

class TestMain(unittest.TestCase):
    @patch('planner.interface.Interface')
    def test_main(self, mock_Interface):
        mock_instance = Mock()
        mock_Interface.return_value = mock_instance
        
        main()
        
        mock_instance.display_menu.assert_called_once()

if __name__ == '__main__':
    unittest.main()
