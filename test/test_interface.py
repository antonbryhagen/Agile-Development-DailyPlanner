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
                call.Button(text='Back'),
                call.Button().pack(),
                call.Button().bind("<Button>", self.interface.return_to_main_page),
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
    
    def test_bind_buttons2(self,):
        test_object = interface.Interface()
        mock_button = MagicMock()
        mock_button.bind.return_value = 'return'
        test_object.button3 = mock_button
        test_object.button4 = mock_button
        mock_self = MagicMock()
        interface.Interface.bind_buttons2(mock_self)
        self.assertEqual(test_object.button3.bind.return_value, 'return')
        self.assertEqual(test_object.button4.bind.return_value, 'return')


    @patch("planner.interface.Interface.bind_buttons2")
    def test_welcome(self, mock_buttons):
        name = "test"
        mock_bind_buttons2 = MagicMock()
        mock_buttons.return_value = mock_bind_buttons2
        self.interface.welcome(name)
        mock_buttons.assert_called_once()
        self.interface.welcome_window.destroy()

    @patch("planner.interface.Interface.welcome")
    def test_get_activity_data(self, mock_welcome):
        # create mock objects
        mock_welcome_method = MagicMock()
        mock_welcome.return_value = mock_welcome_method
        event = MagicMock()
        mock_activities = MagicMock()
        mock_activities.get.return_value = "Activity 1"
        mock_time = MagicMock()
        mock_time.get.return_value = "2"
        mock_clicked = MagicMock()
        mock_clicked.get.return_value = "Vary important"
        mock_user = MagicMock()
        mock_user.get.return_value = "test"
        mock_activities_object = MagicMock()
        mock_user_DAO_handler = MagicMock()
        mock_welcome_window = MagicMock()

        # create test_object
        test_object = interface.Interface()
        test_object.activity = mock_activities
        test_object.time = mock_time
        test_object.clicked = mock_clicked
        test_object.user_object = mock_user
        test_object.activities_object = mock_activities_object
        test_object.user_DAO_handler = mock_user_DAO_handler
        test_object.welcome_window = mock_welcome_window

        test_object.get_activity_data(event)

        # assert that the correct calls were made
        mock_activities.get.assert_called_once()
        mock_time.get.assert_called_once()
        mock_welcome_window.destroy.assert_called_once()
        test_object.welcome.assert_called_once_with(test_object.user_object.name)

    @patch('tkinter.Label')
    @patch('tkinter.Button')
    @patch('tkinter.Entry')
    @patch("planner.interface.Interface.get_activity_data")
    def test_input_activity(self, mock_get_activity_data, mock_entry, mock_button, mock_label):
        mock_event = MagicMock()
        mock_button3 = MagicMock()
        mock_button4 = MagicMock()
        mock_get_data = MagicMock()
        mock_schedule_button = MagicMock()
        mock_get_activity_data = mock_get_data
        test_object = interface.Interface()
        test_object.button3 = mock_button3
        test_object.button4 = mock_button4
        test_object.view_schedule_button = mock_schedule_button
        test_object.get_activity_data = mock_get_activity_data
        test_object.input_activity(mock_event)
        mock_button.assert_any_call(text='Back')
        mock_entry.assert_any_call(width=50)
        mock_entry.return_value.pack.assert_any_call()
        mock_label.assert_called_with(text='Priority:')

    @patch('planner.interface.Interface.welcome')
    def test_get_activity_data_delete(self, mock_welcome):
        mock_dao_handler = MagicMock()
        mock_window = MagicMock()
        mock_clicked = MagicMock()
        mock_welcome_method = MagicMock()
        mock_welcome.return_value = mock_welcome_method
        mock_event = MagicMock()
        mock_user = MagicMock()
        mock_name = 'name'
        test_object = interface.Interface()
        test_object.user_DAO_handler = mock_dao_handler
        test_object.welcome_window = mock_window
        test_object.user_object = mock_user
        test_object.user_object.name = mock_name
        test_object.clicked = mock_clicked
        test_object.get_activity_data_delete(mock_event)
        mock_window.destroy.assert_called_once()
        test_object.welcome.assert_called_once_with(test_object.user_object.name)

    @patch('tkinter.Label')
    @patch('tkinter.Button')
    def test_input_activity_delete(self, mock_button, mock_label):
        mock_buttons = MagicMock()
        mock_event = MagicMock()
        mock_schedule_button = MagicMock()
        mock_user = MagicMock()
        mock_DAO_handler = MagicMock()
        mock_DAO_handler.get_activities.return_value = [['1', '2', '3']]
        test_object = interface.Interface()
        test_object.button3 = mock_buttons
        test_object.button4 = mock_buttons
        test_object.view_schedule_button = mock_schedule_button
        test_object.user_object = mock_user
        test_object.user_DAO_handler = mock_DAO_handler
        test_object.input_activity_delete(mock_event)
        mock_button.assert_called_with(text='Delete')

    def tearDown(self):
        self.interface = None


class TestSchedule(unittest.TestCase):

    def test_generate_new_schedule(self):
        # Create a mock event object
        event = "mock_event"

        # Create a mock user object
        class UserObject:
            username = "mock_username"
        
        user_object = UserObject()

        # Create a mock schedule_window and schedule_handler objects
        class MockWindow:
            def destroy(self):
                pass

        class MockScheduleHandler:
            def delete_schedule(self, username):
                pass

        mock_window = MockWindow()
        mock_schedule_handler = MockScheduleHandler()

        # Create an instance of the class containing the generate_new_schedule method
        class ScheduleClass:
            def __init__(self, schedule_window, schedule_handler, user_object):
                self.schedule_window = schedule_window
                self.schedule_handler = schedule_handler
                self.user_object = user_object

            def generate_new_schedule(self, event):
                self.schedule_window.destroy()
                generate_schedule = True
                self.schedule_handler.delete_schedule(self.user_object.username)
                self.schedule(generate_schedule)

            def schedule(self, generate_schedule):
                # Implement the schedule method here or provide a mock implementation
        
        # Create an instance of the ScheduleClass
                schedule_obj = ScheduleClass(mock_window, mock_schedule_handler, user_object)

        # Call the generate_new_schedule method
                schedule_obj.generate_new_schedule(event)

        # Add assertions to check the expected behavior
        self.assertTrue(mock_window.destroy_called)
        self.assertTrue(mock_schedule_handler.delete_schedule_called)
        # Add more assertions as needed

if __name__ == "__main__":
    unittest.main()
