import unittest
from unittest.mock import MagicMock, patch, call, ANY
from planner import interface


class TestInterface(unittest.TestCase):
    def setUp(self):
        self.interface = interface.Interface()

    @patch("planner.interface.tk")
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

    @patch("planner.interface.Interface.input_menu")
    @patch("planner.interface.tk")
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

    @patch("planner.interface.Interface.input_menu")
    @patch("planner.interface.tk")
    def test_register_user_menu(self, mock_tk, mock_input_menu):
        # create mock objects for header Label and input_menu
        mock_in_menu = MagicMock()

        # return value of mock_input_menu and mock_tk set to mock objects
        mock_input_menu.return_value = mock_in_menu

        # call methods to be tested
        e = ""  # register_user_menu require argument but is never used
        self.interface.register_user_menu(e)

        # make assertions
        mock_tk.assert_has_calls(
            [
                call.Label(text="Register new user"),
                call.Label().pack(),
                call.Label(text="Name:"),
                call.Label().pack(),
                call.Entry(width=50),
                call.Entry().pack(),
                call.Button(text="Register"),
                call.Button().pack(),
            ]
        )

    @patch("planner.interface.tk")
    def test_input_menu(self, mock_tk):
        mock_greeting = MagicMock()
        mock_button1 = MagicMock()
        mock_button2 = MagicMock()

        self.interface.greeting = mock_greeting
        self.interface.button1 = mock_button1
        self.interface.button2 = mock_button2

        # call method to be tested
        self.interface.input_menu()

        # make assertions
        mock_tk.assert_has_calls(
            [
                call.Label(text="Username:"),
                call.Label().pack(),
                call.Entry(width=50),
                call.Entry().pack(),
                call.Label(text="Password:"),
                call.Label().pack(),
                call.Entry(width=50),
                call.Entry().pack(),
            ]
        )

    @patch("planner.interface.Interface.destroy_window")
    def test_get_register_data_register(self, mock_destroy_window):
        mock_username = MagicMock()
        mock_password = MagicMock()
        mock_name = MagicMock()
        mock_DAO_handler = MagicMock()
        mock_destroy_win = MagicMock()
        mock_username.get.return_value = "TestUser"
        mock_password.get.return_value = "TestPassword"
        mock_name.get.return_value = "Test"
        self.interface.username = mock_username
        self.interface.password = mock_password
        self.interface.name = mock_name
        self.interface.user_DAO_handler = mock_DAO_handler
        mock_destroy_window.return_value = mock_destroy_win

        e = ""
        action_type = "register"
        self.interface.get_register_data(e, action_type)
        self.assertEqual(self.interface.user_username, "TestUser")
        self.assertEqual(self.interface.user_name, "Test")
        self.assertEqual(self.interface.user_password, "TestPassword")
        mock_DAO_handler.create_user.assert_called_once()

    @patch("planner.interface.Interface.welcome")
    def test_get_register_data_login(self, mock_welcome):
        mock_username = MagicMock()
        mock_password = MagicMock()
        mock_welc = MagicMock()
        mock_DAO_handler = MagicMock()
        mock_user_object = MagicMock()
        mock_username.get.return_value = "TestUser"
        mock_password.get.return_value = "TestPassword"
        mock_DAO_handler.get_user_by_username.return_value = ["TestUser", "Test"]
        self.interface.username = mock_username
        self.interface.password = mock_password
        self.interface.user_DAO_handler = mock_DAO_handler
        self.interface.user_object = mock_user_object
        mock_welcome.return_value = mock_welc

        e = ""
        action_type = "login"
        self.interface.get_register_data(e, action_type)
        self.assertEqual(self.interface.user_username, "TestUser")
        self.assertEqual(self.interface.user_password, "TestPassword")
        mock_DAO_handler.get_user_by_username.assert_called_once()
        mock_welcome.assert_called_once()

    @patch("planner.interface.Interface.display_menu")
    def test_destroy_window(self, mock_display_menu):
        mock_window = MagicMock()
        mock_display_men = MagicMock()
        mock_display_menu.return_value = mock_display_men
        self.interface.window = mock_window
        self.interface.destroy_window()
        mock_window.destroy.assert_called_once()
        mock_display_menu.assert_called_once()

    def tearDown(self):
        self.interface = None


if __name__ == "__main__":
    unittest.main()
