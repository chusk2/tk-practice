"""Password generator interface"""
# http://www.passwordmeter.com/

from pathlib import Path as pth
from tkinter import messagebox
import tkinter as tk
import json
from passwd_generator import gen_passwd


window = tk.Tk()
window.title('Password Generator')


main_frame = tk.Frame(window)
main_frame.grid(row=0, column=0, padx=10, pady=10)
# website form
website_lbl = tk.Label(main_frame, text='Website')
website_lbl.grid(row=0, column=0, sticky='e', padx=15, pady=5)
website_SV = tk.StringVar()
website_entry = tk.Entry(main_frame, textvariable=website_SV, width=30)
website_entry.grid(row=0, column=1)

# user form
user_lbl = tk.Label(main_frame, text='Username')
user_lbl.grid(row=1, column=0, sticky='e', padx=15, pady=5)
username_SV = tk.StringVar()
user_entry = tk.Entry(main_frame, textvariable=username_SV, width=30)
user_entry.grid(row=1, column=1)

# password form
password_lbl = tk.Label(main_frame, text='Password')
password_lbl.grid(row=2, column=0, sticky='e', padx=15, pady=5)
password_SV = tk.StringVar()
password_entry = tk.Entry(main_frame, textvariable=password_SV, width=30)
password_entry.grid(row=2, column=1)

# create functions to validate data and store passwords


def set_passwd():
    """fill password field with given
    or generated password"""
    if not password_SV.get():
        password_SV.set(gen_passwd())


def clean_form():
    """ Clean form values"""
    website_SV.set('')
    username_SV.set('')
    password_SV.set('')


def save():
    """Stores the website, username, and password in the database"""
    website_ = website_SV.get()
    username_ = username_SV.get()
    password_ = password_SV.get()
    form_content = {
        'website': website_,
        'username': username_,
        'password': password_,
    }
    # Check if any form content is missing,
    # otherwise show warning and do not save form content
    for key, value in form_content.items():
        if not value:
            messagebox.showerror('Missing field', f'{key} was not provided!')
            return
    # create dictionary to store in json file
    # get StringVars content

    # aks for confirmation to store password
    msg = f"""Store password?
    {website_}
    User: {username_}
    Pass: {password_}"""

    confirm = messagebox.askokcancel(title='Confirmation', message=msg)

    if confirm:
        dic = {
            website_: {
                'username': username_,
                'password': password_,
            }
        }

        home = pth.cwd()
        file = home / 'stored_passwords.json'
        # if file exists, the update its content
        if file.exists():
            # read the existing data
            with open('stored_passwords.json', 'r', encoding='utf8') as f:
                data_passwords = json.load(f)
                # update the stored passwords
                data_passwords.update(dic)
            # write the updated data to json file
            with open('stored_passwords.json', 'w', encoding='utf8') as f:
                json.dump(data_passwords, f, indent=4)
        # create a new json file
        else:
            with open('stored_passwords.json', 'w', encoding='utf8') as f:
                json.dump(dic, f, indent=4)

        clean_form()
    # suggested data are not to be stored
    # in that case, keep website and username
    # but remove suggested password
    else:
        password_SV.set('')
        password_entry.focus_set()


# buttons
buttons_frame = tk.Frame(window)
buttons_frame.grid(row=1, column=0)

# pass generator button
generate_btn = tk.Button(buttons_frame, text='Generate Password',
                         command=set_passwd)
generate_btn.grid(row=0, column=0, sticky='w', padx=5, pady=10)

# clean password field button
reset_pass_entry_btn = tk.Button(buttons_frame, text='Clean password',
                                 command=lambda : password_SV.set(''))
reset_pass_entry_btn.grid(row=0, column=1, sticky='w', padx=5, pady=10)

# create the save button
save_btn = tk.Button(buttons_frame, text='Save Password',
                     command=save)
save_btn.grid(row=1, column=0, sticky='we', padx=5, pady=10)

# create clean form button
clean_btn = tk.Button(buttons_frame, text='Clean form',
                      command=clean_form)
clean_btn.grid(row=1, column=1, sticky='we', padx=5, pady=10)



window.mainloop()
