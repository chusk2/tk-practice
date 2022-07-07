import tkinter as tk
from tkinter import StringVar, ttk
from sympy import resultant

window = tk.Tk()

window.geometry('600x700')
window.title('Check buttons')
window.resizable(0,1)

# LabelFrame
lbl_frm1 = tk.LabelFrame(text=' Checkbuttons ')
lbl_frm1.grid(row=0, column=0, sticky='w', padx=10, pady=10)

# Checkbutton

options = []
options_vars = []
for i in range(3):
    # create a Checkbutton
    options.append(ttk.Checkbutton(lbl_frm1))
    # create a IntVar to store its status
    options_vars.append(tk.IntVar())
    options[-1].configure(text=f'Option {i+1}',
    # variable to store checkbutton status
    variable = options_vars[i],
    # values of variable depending on
    # whether checkbutton is marked or not
    # default values for onvalue and offvalue are (1) True, (0) False
    onvalue=i,
    offvalue=0
    )
    options[-1].grid(row=i, column=0, sticky='w', padx=10)

    """def show_results():
        for index, value in enumerate(options_vars):
            if value.get():
                print(f'Option {index + 1} is marked.')"""

def show_results():
    for index, value in enumerate(options_vars):
            if value.get():
                print(f'Option {index + 1} has a value of: {value.get()}.')

checkbtn_btn = tk.Button(lbl_frm1, text='Show results', command=show_results)
checkbtn_btn.grid(row=4, column=0, padx=10)

# LabelFrame
lbl_frm2 = tk.LabelFrame(text=' Radio buttons ')
lbl_frm2.grid(row=2, column=0, sticky='w', padx=10, pady=10)

# Radio buttons

radio_options_widgets = []
radio_options = [f'Exclusive option no. {i}' for i in range(5)]
radio_option_var = tk.StringVar()

def radio_results():
    print(radio_option_var.get())

for i in range(5):
    radio_options_widgets.append(ttk.Radiobutton(lbl_frm2))
    radio_options_widgets[-1].configure(
    text=f'Exclusive option {i+1}',
    variable = radio_option_var,
    value=f'Selection no. {i+1}',
    command=radio_results,)
    radio_options_widgets[-1].grid(row=i, column=0, sticky='w', padx=10)

# Button
radio_btn = tk.Button(lbl_frm2, text='Radio selected option', command=radio_results)
radio_btn.grid(row=5, column=0, padx=10)

# LabelFrame
lbl_frm3 = tk.LabelFrame(text=' Combo box ')
lbl_frm3.grid(row=3, column=0, sticky='w', padx=10, pady=10)

# Combo box
combo_var = tk.StringVar()
combo = ttk.Combobox(lbl_frm3,
                    textvariable=combo_var,
                    values = [f'Combo option {i}' for i in range(5)],
                    justify='left')
combo.grid(row=0, column=0, padx=10, pady=15)

txt = tk.StringVar()
lbl = ttk.Label(lbl_frm3,
                textvariable=txt,
                font=('Courier', 9))
lbl.grid(row=1, column=0, padx=10)

def get_value():
    txt.set(f'Option selected: {combo.get()}')

btn = ttk.Button(lbl_frm3,text='Get combo box value', command=get_value)
btn.grid(row=1, column=1)

# entry
passwd = tk.StringVar()
ntry = ttk.Entry(width=15, textvariable=passwd)
ntry.grid(row=14, column=0)

def get_value():
    txt.set(passwd.get())

btn_entry = ttk.Button(text='Get entry value', command=get_value)
btn_entry.grid(row=14, column=1)

# Text
txt_widget = tk.Text(undo=True,
                    width=35,
                    wrap='word',
                    spacing1 = 2, spacing2 = 5,
                    )
txt_widget.grid(row=15, column=0, padx=10, pady=10)

window.mainloop()
