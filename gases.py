"""Calculator for perfect gases using equation: PV = nRT"""
from email.mime import image
import tkinter as tk
from tkinter import messagebox

from numpy import column_stack


window = tk.Tk()
window.geometry('450x400')
window.title('Calculadora gases perfectos')
window.config(padx=10, pady=10)

bg_img = tk.PhotoImage(file='chemistry.png')
bg_frame = tk.Label(window, image=bg_img)
bg_frame.place(x=0, y=0, relwidth =1, relheight=1)

# canvas = tk.Canvas(width=500, height=500)
# canvas.create_image(250, 250, image=background_img)
# canvas.grid(row=0, column=0)

title = tk.Label(bg_frame, text='PV = nRT',
    font=('Verdana', 35, 'bold'),
    bg='white', fg='lightblue')
title.grid(row=0, column=0, columnspan=2, sticky='we')

#TODO inferir la incógnita a partir del entry vacío
# frame to select the unknown of the equation
unknown_frame = tk.LabelFrame(bg_frame, text=' Unknown variable ',
    bg='white', padx=10, pady=10)
unknown_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nw')

unknown_radiobuttons = []
unknown_var = tk.StringVar()
for index, var in enumerate(['P','V', 'n', 'T']):
    unknown_radiobuttons.append(
        tk.Radiobutton(unknown_frame,
            text=var,
            value=var,
            variable=unknown_var,
            bg='white', padx=5)
    )
    unknown_radiobuttons[-1].grid(row=0, column=index)

# Variable values form
variables_frame = tk.LabelFrame(bg_frame, text=' Variable Values ',
    bg='white', padx=10, pady=10)
variables_frame.grid(row=1, column=1, sticky='ne')

variables_fields = {}
variables_labels = ['Pressure', 'Volume', 'moles', 'Temperature']
variables_vars = [tk.StringVar() for i in variables_labels]
# create a pair of (label,entry) for each variable in equation
for index, value in enumerate(variables_labels):
    variables_fields[value] = [
        tk.Label(variables_frame, text=value, bg='white'),
        tk.Entry(variables_frame, width=10,
            textvariable=variables_vars[index],
            bg='white')
    ]
    variables_fields[value][0].grid(row=index, column=0, sticky='e')  # label
    variables_fields[value][1].grid(row=index, column=1, sticky='e')  # entry

#TODO show result in the previously empty field, using bold and coloured font
# results
result_frame = tk.LabelFrame(bg_frame, text=' Solve equation ',
    bg='white', padx=10, pady=10)
result_frame.grid(row=2, column=0, padx=10, pady=10, sticky='we',
    columnspan=2)

result_label = tk.Label(result_frame, text='', bg='white')
result_label.grid(row=0, column=1, padx=10, pady=10)


def clean():
    """Reset all entry fields values"""
    for index in range(len(variables_labels)):
        variables_vars[index].set('')
    result_label.config(text='')

def solve():
    """Solve the ecuation and show the result"""
    R = 0.082
    proceed = True  # equation can be solved
    unknown = unknown_var.get()
    # get variable values
    # variables_fields[variable][1].get()


    def float_conversion(varname):
        string = variables_fields[varname][1].get()
        if string != '':
            try:
                return float(string)
            except ValueError:
                messagebox.showerror('Wrong type',
                    f'Introduce a numerical value for the {varname.lower()}')
                #FIXME improve the way it checks if equation can be solved
                proceed = False
        else:
            return None  # ignore this variable


    p = float_conversion('Pressure')
    v = float_conversion('Volume')
    n = float_conversion('moles')
    temp = float_conversion('Temperature')
        
    # solve equations
    if unknown == 'P' and proceed:
        result_eq = n*R*temp/v
        result_label.config(text=f'Resutl: {result_eq:.3f} atm')

    elif unknown == 'V' and proceed:
        result_eq = n*R*temp/p
        result_label.config(text=f'Result: {result_eq:.3f} L')

    elif unknown == 'T' and proceed:
        result_eq = p*v/(n*R)
        text_ = f'Result: {result_eq:.3f} K = ' \
                f'{result_eq - 273:.3f} Celsius degrees'
        result_label.config(text=text_)

    elif unknown == 'n' and proceed:
        result_eq = p*v/(R*temp)
        result_label.config(text=f'Result: {result_eq:.3f} mol')

solve_button = tk.Button(result_frame, text='Solve equation',
    command=solve, bg='white')
solve_button.grid(row=0, column=0, padx=5, pady=5, sticky='w')

reset_button = tk.Button(result_frame, text='Reset values',
    command=clean, bg='white')
reset_button.grid(row=1, column=0, padx=5, pady=5, sticky='w')

window.mainloop()
