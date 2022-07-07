"""Password generator interface"""
# http://www.passwordmeter.com/

from pathlib import Path as pth
from tkinter import messagebox
import tkinter as tk
from passwd_generator import gen_passwd


window = tk.Tk()
window.title('Password Generator')


main_frame = tk.Frame(window)
main_frame.grid(row=1, column=0, padx=10, pady=10)
# website form
website_lbl = tk.Label(main_frame, text='Website')
website_lbl.grid(row=0, column=0, sticky='e', padx=15, pady=5)
website = tk.StringVar()
website_entry = tk.Entry(main_frame, textvariable=website, width=30)
website_entry.grid(row=0, column=1)

# user form
user_lbl = tk.Label(main_frame, text='Username')
user_lbl.grid(row=1, column=0, sticky='e', padx=15, pady=5)
username = tk.StringVar()
user_entry = tk.Entry(main_frame, textvariable=username, width=30)
user_entry.grid(row=1, column=1)

# password form
password_lbl = tk.Label(main_frame, text='Password')
password_lbl.grid(row=2, column=0, sticky='e', padx=15, pady=5)
password = tk.StringVar()
password_entry = tk.Entry(main_frame, textvariable=password, width=30)
password_entry.grid(row=2, column=1)

# generate password button


def set_passwd():
    """fill password field with given
    or generated password"""
    if not password.get():
        password.set(gen_passwd())


def check_form():
    """Check if any form content is missing,
    otherwise show warning"""
    form_content = {
        'website' : website.get(),
        'ursername' : username.get(),
        'password' : password.get(),
    }
    for key, value in form_content.items():
        if not value:
            messagebox.showerror('Missing field',
                f'{key} was not provided!')
            return False
    line = ''
    for value in form_content.values():
        line += f'{value}\t| '
    line += '\n'
    return line


def save():
    """Stores the website, username, and password in the database"""
    password_line = check_form()
    if password_line:
        home = pth.cwd()
        file = home / 'password_store.txt'
        if file.exists():
            with open('password_store.txt', 'a', encoding='utf8') as f:
                f.writelines(password_line)
        else:
            with open('password_store.txt', 'w', encoding='utf8') as f:
                header = 'website | username | password\n'
                f.writelines(header)
                f.writelines(password_line)

generate_btn = tk.Button(main_frame, text='Generate Password',
    command=set_passwd)
generate_btn.grid(row=3, column=0, sticky='e')

save_btn = tk.Button(main_frame, text='Save Password',
    command=save)
save_btn.grid(row=3, column=1, sticky='e')


window.mainloop()
