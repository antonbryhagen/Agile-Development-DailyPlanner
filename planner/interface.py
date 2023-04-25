import tkinter as tk
import user
import user_DAO


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
            
        elif action_type == "login":
            self.user_DAO_handler.get_user_by_username(user_username, user_password)
        self.destroy_window()
    
    def destroy_window(self):
        self.window.destroy()
        self.display_menu()

    def bind_buttons(self):
        self.button1.bind("<Button>", self.log_in_menu)
        self.button2.bind("<Button>", self.register_user_menu)
        self.window.mainloop()
