import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello")
greeting.pack()
button1 = tk.Button(text="Log in")
button2 = tk.Button(text="Register")
button1.pack()
button2.pack()


def log_in_menu(event):
    header = tk.Label(text="Log in")
    header.pack()
    input_menu()
    log_in = tk.Button(text="Log In")
    log_in.pack()


def register_user_menu(event):
    header = tk.Label(text="Register new user")
    header.pack()
    input_menu()
    register = tk.Button(text="Register")
    register.pack()


def input_menu():
    greeting.destroy()
    button1.destroy()
    button2.destroy()
    label_username = tk.Label(text='Username:')
    label_username.pack()
    username = tk.Entry(width=50)
    username.pack()
    label_password = tk.Label(text='Password:')
    label_password.pack()
    password = tk.Entry(width=50)
    password.pack()


button1.bind("<Button>", log_in_menu)
button2.bind("<Button>", register_user_menu)

window.mainloop()
