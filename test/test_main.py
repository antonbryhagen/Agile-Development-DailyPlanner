"""Testing main"""
import unittest
from unittest.mock import patch, Mock
from planner import main

class TestMain(unittest.TestCase):
    """Class for testing main."""
    @patch('planner.interface.Interface')
    def test_main(self, mock_Interface):
        """Test main function of main."""
        # Create mock object for interface instance in main
        # Use mock object to call display_menu function
        # As if ui variable in main is replaced with mock_instance
        mock_instance = Mock()
        mock_Interface.return_value = mock_instance
        
        main.main()
        
        mock_instance.display_menu.assert_called_once()

if __name__ == '__main__':
    unittest.main()
