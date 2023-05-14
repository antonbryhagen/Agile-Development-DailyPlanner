import tkinter as tk
from planner import user
from planner import user_DAO
from planner import Activities
from planner import schedule_DAO
from planner import schedule
from tkinter import *


class Interface:
    def __init__(self):
        self.user_DAO_handler = user_DAO.user_DAO()
        self.schedule_handler = schedule_DAO.Schedule_DAO()

    def display_menu(self):
        self.window = tk.Tk()
        self.window.geometry("250x250")
        self.greeting = tk.Label(text="Hello")
        self.greeting.pack()
        self.button1 = tk.Button(text="Log in")
        self.button2 = tk.Button(text="Register")
        self.button1.pack()
        self.button2.pack()
        self.bind_buttons()

    def log_in_menu(self, event):
        self.header = tk.Label(text="Log in")
        self.header.pack()
        self.input_menu()
        self.log_in = tk.Button(text="Log In")
        self.log_in.pack()
        self.log_in.bind(
            "<Button>", lambda event: self.get_register_data(event, "login")
        )

    def register_user_menu(self, event):
        self.header = tk.Label(text="Register new user")
        self.header.pack()
        self.input_menu()
        self.label_name = tk.Label(text="Name:")
        self.label_name.pack()
        self.name = tk.Entry(width=50)
        self.name.pack()
        self.register = tk.Button(text="Register")
        self.register.pack()
        self.register.bind(
            "<Button>", lambda event: self.get_register_data(event, "register")
        )

    def input_menu(self):
        self.greeting.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.label_username = tk.Label(text="Username:")
        self.label_username.pack()
        self.username = tk.Entry(width=50)
        self.username.pack()
        self.label_password = tk.Label(text="Password:")
        self.label_password.pack()
        self.password = tk.Entry(width=50)
        self.password.pack()

    def get_register_data(self, event, action_type):
        self.user_username = self.username.get()
        self.user_password = self.password.get()
        if action_type == "register":
            self.user_name = self.name.get()
            self.user_object = user.User(
                self.user_username, self.user_name, self.user_password
            )
            self.user_DAO_handler.create_user(self.user_object)
            self.destroy_window()

        elif action_type == "login":
            result = self.user_DAO_handler.get_user_by_username(
                self.user_username, self.user_password
            )
            if result != False:
                self.user_object = user.User(result[0], result[1], "")
                self.window.destroy()
                self.welcome(self.user_object.name)

    def destroy_window(self):
        self.window.destroy()
        self.display_menu()

    def welcome(self, name):
        
        self.welcome_window = tk.Tk()
        self.welcome_window.geometry("250x250")
        self.welcome_text = tk.Label(text="Welcome: " + name)
        self.welcome_text.pack()
        self.button3 = tk.Button(text="Add activities")
        self.button3.pack()
        self.button4 = tk.Button(text="Remove activities")
        self.button4.pack()
        self.view_schedule_button = tk.Button(text="View schedule")
        self.view_schedule_button.pack()
        self.bind_buttons2()
        self.welcome_window.mainloop()

    def bind_buttons(self):
        self.button1.bind("<Button>", self.log_in_menu)
        self.button2.bind("<Button>", self.register_user_menu)
        self.window.mainloop()

    def bind_buttons2(self):
        self.button3.bind("<Button>", self.input_activity)
        self.button4.bind("<Button>", self.input_activity_delete)
        self.view_schedule_button.bind("<Button>", self.schedule)
        self.window.mainloop()

    # def add_activities_menu(self):
    # header = tk.Label(text="Add activities")
    # header.pack()
    # label_activity = tk.Label(text='Activity:')
    # label_activity.pack()
    # self.activity = tk.Entry(width=50)
    # self.activity.pack()
    # self.add_activity = tk.Button(text="Add activity")
    # self.add_activity.pack()
    # self.add_activity.bind("<Button>", self.get_activity_data)
    # self.window.mainloop()

    def get_activity_data(self, event):
        activities_activity = self.activity.get()
        activities_time = self.time.get()
        self.activities_object = Activities.Activities(
            activities_activity, self.PRIO, activities_time, self.user_object.username
        )
        self.user_DAO_handler.create_activity(self.activities_object)
        self.welcome_window.destroy()
        self.welcome(self.user_object.name)

    def input_activity(self, event):
        self.button3.destroy()
        self.button4.destroy()
        label_activity = tk.Label(text="Name of activity:")
        label_activity.pack()
        self.activity = tk.Entry(width=50)
        self.activity.pack()
        label_time = tk.Label(text="Hours of work:")
        label_time.pack()
        self.time = tk.Entry(width=50)
        self.time.pack()
        label_prio = tk.Label(text="Priority:")
        label_prio.pack()
        clicked = StringVar(label_prio)
        optionList = ["Very important", "Important", "Not so important"]
        clicked.set(optionList[0])
        drop = OptionMenu(label_prio, clicked, *optionList).pack()
        clickedOption = clicked.get()
        self.PRIO = clickedOption
        self.button5 = tk.Button(text="Confirm")
        self.button5.pack()
        self.button5.bind("<Button>", self.get_activity_data)
        label_prio.mainloop()

    def get_activity_data_delete(self, event):
        activities_activity_delete = self.activity.get()
        activities_object = Activities.Activities(
            activities_activity_delete, "test", "test1", "test3"
        )
        self.user_DAO_handler.delete_activity(activities_object)
        self.welcome_window.destroy()
        self.welcome(self.user_object.name)

    def input_activity_delete(self, event):
        self.button3.destroy()
        self.button4.destroy()
        label_activity = tk.Label(text="Name of activity:")
        label_activity.pack()
        self.activity = tk.Entry(width=50)
        self.activity.pack()
        self.button6 = tk.Button(text="Delete")
        self.button6.pack()
        self.button6.bind(
            "<Button>", lambda event: self.get_activity_data_delete("Delete")
        )
        label_activity.mainloop()
    
    def schedule(self, event):
        if (event is not True):
            self.welcome_window.destroy()
        self.schedule_window = tk.Tk(className="Schedule")
        schedule_width = "1000"
        schedule_height = "500"
        self.schedule_window.geometry(schedule_width+"x"+schedule_height)
        # TODO
        # Add GUI option for wake hours
        back_button = tk.Button(text="Back")
        back_button.place(relx=0.95, rely=0, anchor='ne')
        back_button.bind("<Button>", self.go_back_schedule)
        generate_schedule_button = tk.Button(text="Generate a new schedule")
        generate_schedule_button.place(relx=0.9, rely=0, anchor='ne')
        generate_schedule_button.bind("<Button>", self.generate_new_schedule)
        wake_hours = 8
        user_schedule = schedule.Schedule(self.user_DAO_handler.get_activities(self.user_object), wake_hours)
        stored_schedule = self.schedule_handler.get_schedule(self.user_object.username)
        if stored_schedule == []:
            user_schedule.sort_activities()
            self.schedule_handler.create_schedule(user_schedule.activities, self.user_object.username)
        else:
            # Reset user_schedule dictionaries before loading stored schedule
            user_schedule.time_per_day = {
            "Monday" : user_schedule.wake_hours,
            "Tuesday" : user_schedule.wake_hours,
            "Wednesday" : user_schedule.wake_hours,
            "Thursday" : user_schedule.wake_hours,
            "Friday" : user_schedule.wake_hours,
            "Saturday" : user_schedule.wake_hours,
            "Sunday" : user_schedule.wake_hours
            }
            user_schedule.days = {
            "Monday" : [],
            "Tuesday" : [],
            "Wednesday" : [],
            "Thursday" : [],
            "Friday" : [],
            "Saturday" : [],
            "Sunday" : []
            }
            sorted(stored_schedule, key=lambda scheduled_activity: scheduled_activity[2])
            temp_activties = []
            for scheduled_activity in stored_schedule:
                for act in user_schedule.activities:
                    if scheduled_activity[1] == act[3]:
                        temp_activties.append(act)
                        
            user_schedule.activities = temp_activties
        user_schedule.generate_schedule()
        week_days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
        week_labels = []
        activity_labels = []
        for day_index in range(0, 7): 
            week_labels.append(tk.Label(text=week_days[day_index], font='bold'))
            week_labels[day_index].place(relx=0.12*(1+day_index), rely=0.05, anchor='nw')
            gray_background = False
            start_rely = 75/int(schedule_height) # 0.1 with height 500, good starting point in y direction
            activity_width = 120 # width of activity in schedule in px
            activity_height = 25 # height of activity in schedule in px for one hour
            for activity in user_schedule.days[week_days[day_index]]:
                activity_labels.append(tk.Label(text=activity[0]))
                activity_labels[-1].place(relx=0.12*(1+day_index), rely=start_rely, anchor='nw', width=activity_width, height=activity_height*activity[2])
                start_rely += activity_height*activity[2]/int(schedule_height)
                if gray_background:
                    activity_labels[-1].config(bg="gray51", fg="white", borderwidth=1, relief="solid")
                    gray_background = False
                elif not gray_background:
                    activity_labels[-1].config(borderwidth=1, relief="solid")
                    gray_background = True

        self.schedule_window.mainloop()

    def go_back_schedule(self, event):
        self.schedule_window.destroy()
        self.welcome(self.user_object.name)
    
    def generate_new_schedule(self, event):
        self.schedule_window.destroy()
        generate_schedule = True
        self.schedule_handler.delete_schedule(self.user_object.username)
        self.schedule(generate_schedule)
