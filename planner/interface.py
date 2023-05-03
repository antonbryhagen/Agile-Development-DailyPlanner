import tkinter as tk
import user
import user_DAO
import Activities
from tkinter import *


class Interface:

    def __init__(self):
        self.user_DAO_handler = user_DAO.user_DAO()

    def display_menu(self):
        self.window = tk.Tk()
        self.greeting = tk.Label(text="Hello")
        self.greeting.pack()
        self.button1 = tk.Button(text="Log in")
        self.button2 = tk.Button(text="Register")
        self.button1.pack()
        self.button2.pack()
        self.bind_buttons()

    def log_in_menu(self, event):
        header = tk.Label(text="Log in")
        header.pack()
        self.input_menu()
        self.log_in = tk.Button(text="Log In")
        self.log_in.pack()
        self.log_in.bind("<Button>", lambda event: self.get_register_data(event, "login"))

    def register_user_menu(self, event):
        header = tk.Label(text="Register new user")
        header.pack()
        self.input_menu()
        label_name = tk.Label(text='Name:')
        label_name.pack()
        self.name = tk.Entry(width=50)
        self.name.pack()
        self.register = tk.Button(text="Register")
        self.register.pack()
        self.register.bind("<Button>", lambda event: self.get_register_data(event, "register"))

    def input_menu(self):
        self.greeting.destroy()
        self.button1.destroy()
        self.button2.destroy()
        label_username = tk.Label(text='Username:')
        label_username.pack()
        self.username = tk.Entry(width=50)
        self.username.pack()
        label_password = tk.Label(text='Password:')
        label_password.pack()
        self.password = tk.Entry(width=50)
        self.password.pack()

    def get_register_data(self, event, action_type):
        user_username = self.username.get()
        user_password = self.password.get()
        if action_type == "register":
            user_name = self.name.get()
            self.user_object = user.User(user_username, user_name, user_password)
            self.user_DAO_handler.create_user(self.user_object)
            self.destroy_window()

        elif action_type == "login":
            result = self.user_DAO_handler.get_user_by_username(user_username, user_password)
            if result != False:
                self.user_object = user.User(result[0], result[1], "")
                self.welcome(self.user_object.name)


    def destroy_window(self):
        self.window.destroy()
        self.display_menu()

    def welcome(self, name):
        self.window.destroy()
        welcome_window = tk.Tk()
        #name = self.name.get()
        welcome_text = tk.Label(text="Welcome: "+name)
        welcome_text.pack()
        self.button3 = tk.Button(text="Add activities")
        self.button3.pack()
        self.button4 = tk.Button(text="Remove activities")
        self.button4.pack()
        self.bind_buttons2()
        welcome_window.mainloop()

    def bind_buttons(self):
        self.button1.bind("<Button>", self.log_in_menu)
        self.button2.bind("<Button>", self.register_user_menu)
        self.window.mainloop()

    def bind_buttons2(self):
        self.button3.bind("<Button>", self.input_activity)
        self.button5.bind("<Button>", self.get_activity_data)
        self.button4.bind("<Button>", self.get_activity_data_delete)
        self.window.mainloop()

    #def add_activities_menu(self):
        #header = tk.Label(text="Add activities")
        #header.pack()
        #label_activity = tk.Label(text='Activity:')
        #label_activity.pack()
        #self.activity = tk.Entry(width=50)
        #self.activity.pack()
        #self.add_activity = tk.Button(text="Add activity")
        #self.add_activity.pack()
        #self.add_activity.bind("<Button>", self.get_activity_data)
        #self.window.mainloop()

    def get_activity_data(self, event):
        activities_activity = self.activity.get()
        activities_time = self.time.get()
        self.activities_object = Activities.Activities(activities_activity, self.PRIO, activities_time, self.user_object.name)
        self.user_DAO_handler.create_activity(self.activities_object)


    def input_activity(self, event):
        label_activity = tk.Label(text='Name of activity:')
        label_activity.pack()
        self.activity = tk.Entry(width=50)
        self.activity.pack()
        label_time = tk.Label(text='Hours of work:')
        label_time.pack()
        self.time = tk.Entry(width=50)
        self.time.pack()
        label_prio = tk.Label(text='Priority:')
        label_prio.pack()
        clicked = StringVar(label_prio)
        optionList = ["Very important", "Important", "Not so important"]
        clicked.set(optionList[0])
        drop = OptionMenu(label_prio, clicked, *optionList).pack()
        clickedOption = clicked.get()
        self.PRIO = drop
        self.button5 = tk.Button(text="Confirm")
        self.button5.pack()
        self.button5.bind("<Button>", lambda event: self.get_activity_data(event, "Confirm"))
        self.bind_buttons2()
        label_prio.mainloop()
        self.destroy_window() 
        
    
    def get_activity_data_delete(self, event):
        activities_activity = self.activity.get()
        activities_time = self.time.get()
        self.activities_object = Activities.Activities(activities_activity, activities_time, self.user_object.name)
        self.user_DAO_handler.delete_activity(self.activities_object)
        self.destroy_window()        


    def input_activity_delete(self, event):
        label_activity = tk.Label(text='Name of activity:')
        label_activity.pack()
        self.activity = tk.Entry(width=50)
        self.activity.pack()
        self.button4 = tk.Button(text="Delete")
        self.button4.pack()
        self.button4.bind("<Button>", lambda event: self.get_activity_data_delete(event, "Delete"))
        self.bind_buttons2()