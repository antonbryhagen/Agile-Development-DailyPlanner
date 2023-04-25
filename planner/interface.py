import tkinter as tk


class Interface:

    def __init__(self):
        pass

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
        log_in = tk.Button(text="Log In")
        log_in.pack()

    def register_user_menu(self, event):
        header = tk.Label(text="Register new user")
        header.pack()
        self.input_menu()
        label_name = tk.Label(text='Name:')
        label_name.pack()
        name = tk.Entry(width=50)
        name.pack()
        register = tk.Button(text="Register")
        register.pack()


    def input_menu(self):
        self.greeting.destroy()
        self.button1.destroy()
        self.button2.destroy()
        label_username = tk.Label(text='Username:')
        label_username.pack()
        username = tk.Entry(width=50)
        username.pack()
        label_password = tk.Label(text='Password:')
        label_password.pack()
        password = tk.Entry(width=50)
        password.pack()


    def bind_buttons(self):
        self.button1.bind("<Button>", self.log_in_menu)
        self.button2.bind("<Button>", self.register_user_menu)
        self.window.mainloop()
