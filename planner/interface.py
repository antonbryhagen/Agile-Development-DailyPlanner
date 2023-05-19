import tkinter as tk
import re
from planner import user
from planner import user_DAO
from planner import Activities
from planner import schedule_DAO
from planner import schedule
from tkinter import *
from win10toast import ToastNotifier
from datetime import datetime, timedelta


class Interface:
    def __init__(self):
        self.user_DAO_handler = user_DAO.user_DAO()
        self.schedule_handler = schedule_DAO.Schedule_DAO()
        self.toaster = ToastNotifier()

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
            if self.user_username == '' or self.user_password == '' or self.user_name == '':
                self.empty_field = tk.Label(text="One or more field(s) are left empty")
                self.empty_field.pack()
            else:
                self.user_DAO_handler.create_user(self.user_object)
                self.destroy_window()



        elif action_type == "login":
            if self.user_username == "" or self.user_password == "":
                self.invalid_login = tk.Label(text="Invalid login information")
                self.invalid_login.pack()
            else:
                self.result = self.user_DAO_handler.get_user_by_username(
                    self.user_username, self.user_password
            )
                if self.result != False:
                    self.user_object = user.User(self.result[0], self.result[1], "")
                    try:
                        if self.window.state() == 'normal':
                            self.window.destroy()
                    except:
                        print("Tested")
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
        self.PRIO = self.clicked.get()
        self.activities_object = Activities.Activities(
            activities_activity, self.PRIO, activities_time, self.user_object.username
        )
        if activities_activity == '' or activities_time == '':
            self.empty_field = tk.Label(text="One or more field(s) are left empty")
            self.empty_field.pack()
        else:
            self.user_DAO_handler.create_activity(self.activities_object)
            self.welcome_window.destroy()
            self.welcome(self.user_object.name)

    def input_activity(self, event):
        self.button3.destroy()
        self.button4.destroy()
        self.view_schedule_button.destroy()
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
        self.clicked = StringVar(label_prio)
        optionList = ["Very important", "Important", "Not so important"]
        self.clicked.set(optionList[0])
        drop = OptionMenu(label_prio, self.clicked, *optionList)
        drop.pack()
        self.button5 = tk.Button(label_prio, text="Confirm")
        self.button5.pack()
        self.button5.bind("<Button>", self.get_activity_data)
        label_prio.mainloop()

    def get_activity_data_delete(self, event):
        activities_activity_delete = self.clicked.get()
        partitioned_string_activity = activities_activity_delete.partition(" |")
        activities_object = Activities.Activities(
            partitioned_string_activity[0], "test", "test1", "test3"
        )
        self.user_DAO_handler.delete_activity(activities_object, self.user_object)
        self.welcome_window.destroy()
        self.welcome(self.user_object.name)

    def input_activity_delete(self, event):
        self.button3.destroy()
        self.button4.destroy()
        self.view_schedule_button.destroy()
        label_activity = tk.Label(text="Choose an activity to delete:")
        label_activity.pack()
        dropdown = tk.Label()
        dropdown.pack()
        activity_tuple_list = self.user_DAO_handler.get_activities(self.user_object)
        activity_str_list = []
        
        for activity in activity_tuple_list:
            activity_string = activity[0] + " | " + activity[1] + " | " + str(activity[2]) + "hour(s)"
            activity_str_list.append(activity_string)

        self.clicked = StringVar(dropdown)
        self.clicked.set("Click to see your activities")
        drop = OptionMenu(dropdown, self.clicked, *activity_str_list)
        drop.pack()
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
        back_button = tk.Button(text="Back")
        back_button.place(relx=0.95, rely=0, anchor='ne')
        back_button.bind("<Button>", self.go_back_schedule)
        generate_schedule_button = tk.Button(text="Generate a new schedule")
        generate_schedule_button.place(relx=0.9, rely=0, anchor='ne')
        generate_schedule_button.bind("<Button>", self.generate_new_schedule)
        # TODO
        # Add GUI option for wake hours
        start_day_time = 8
        end_day_time = 16
        self.wake_hours = end_day_time - start_day_time
        user_schedule = schedule.Schedule(self.user_DAO_handler.get_activities(self.user_object), self.wake_hours)
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
        hour_labels = []
        hours_head = tk.Label(text="Time", font='bold')
        hours_head.place(relx=0, rely=0.05)
        for hour in range(0, self.wake_hours+1):
            hour_labels.append(tk.Label(text=start_day_time+hour))
            hour_labels[-1].place(relx=0.0, rely=0.15+(hour*40/int(schedule_height)), anchor='nw', width=120, height=40)
            hour_labels[-1].config(borderwidth=1, relief="solid")
        for label in hour_labels:
            label.config(anchor='n')
        for day_index in range(0, 7): 
            week_labels.append(tk.Label(text=week_days[day_index], font='bold'))
            week_labels[day_index].place(relx=0.12*(1+day_index), rely=0.05, anchor='nw')
            gray_background = False
            start_rely = 75/int(schedule_height) # 0.15 with height 500, good starting point in y direction
            activity_width = 120 # width of activity in schedule in px
            activity_height = 40 # height of activity in schedule in px for one hour
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
        self.schedule_window.after(1000, lambda: self.schedule_notification(activity[0], activity[2]))

        self.schedule_window.mainloop()
    
    def schedule_notification(self, activities_object_activity, activities_object_time):
        activity_time = self.wake_hours + activities_object_time
        activity_time_str = str(activity_time)
        if len(activity_time_str) == 1:
            activity_time_hour = f"0{activities_object_time}:00"
        elif len(activity_time_str) == 2:
            activity_time_hour = f"{activities_object_time}:00"
        notification_time = datetime.strptime(activity_time_hour, "%H:%M")
        self.current_date_time_str = str(datetime.today().time())
        self.current_date_time_str_len = self.current_date_time_str[:5]
        self.current_date_date = datetime.strptime(str(datetime.today().date()), "%Y-%m-%d")
        self.current_date_time = datetime.strptime(self.current_date_time_str_len, "%H:%M")
        self.notification_datetime_now = datetime.combine(self.current_date_date.date(), self.current_date_time.time())
        self.notification_datetime_noti = datetime.combine(self.current_date_date.date(), notification_time.time())
        self.time_delta = self.notification_datetime_noti - self.notification_datetime_now
        self.schedule_window.after(1000, lambda: self.check_schedule(activities_object_activity, activities_object_time))
        
    def check_schedule(self, activities_object_activity, activities_object_time):
        if self.time_delta.total_seconds() <= 900 and self.time_delta.total_seconds() >= 892:
            self.schedule_window.after(int(self.time_delta.total_seconds() * 1000), self.send_notification(activities_object_activity, activities_object_time))
        self.schedule_window.after(1000, lambda: self.schedule_notification(activities_object_activity, activities_object_time))

    def send_notification(self, activities_object_activity, activities_object_time):
        self.toaster.show_toast(f"Reminder: {activities_object_activity} scheduled in 15 minutes", duration = 10)
        self.schedule_window.after(60000, lambda: self.schedule_notification(activities_object_activity, activities_object_time))

    def go_back_schedule(self, event):
        self.schedule_window.destroy()
        self.welcome(self.user_object.name)
    
    def generate_new_schedule(self, event):
        self.schedule_window.destroy()
        generate_schedule = True
        self.schedule_handler.delete_schedule(self.user_object.username)
        self.schedule(generate_schedule)
