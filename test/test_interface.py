import unittest
from unittest.mock import MagicMock, patch
from planner import interface

class TestInterface(unittest.TestCase):
    def setUp(self):
        self.interface = interface.Interface()

    @patch('planner.interface.tk')
    def test_display_menu(self, mock_tk):
        # create a MagicMock for the greeting Label
        mock_greeting = MagicMock()

        # set the return value of mock_tk.Label to the greeting MagicMock
        mock_tk.Label.return_value = mock_greeting

        # call the method being tested
        self.interface.display_menu()

        # make assertions
        mock_tk.Tk.assert_called_once()
        mock_tk.Label.assert_called_with(text="Hello")
        mock_greeting.pack.assert_called_once()
        self.assertEqual(self.interface.greeting, mock_greeting)

        # clean up
        self.interface.window.destroy()

   
    @patch('planner.interface.Interface.input_menu')
    @patch('planner.interface.tk')
    def test_log_in_menu(self, mock_tk, mock_input_menu):
        # create mock objects for header Label and input_menu
        mock_header = MagicMock()
        mock_in_menu = MagicMock()
        
        # return value of mock_input_menu and mock_tk set to mock objects
        mock_input_menu.return_value = mock_in_menu
        mock_tk.Label.return_value = mock_header
        
        # call methods to be tested
        e = ""  # log_in_menu require argument but is never used
        self.interface.log_in_menu(e)
        
        # make assertions
        mock_tk.Label.assert_called_with(text="Log in")
        mock_header.pack.assert_called_once()
        self.assertEqual(self.interface.header, mock_header) 
        
    
    
    def tearDown(self):
        self.interface = None

if __name__ == '__main__':
    unittest.main()
