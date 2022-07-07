import tkinter as tk

from sympy import resultant

window = tk.Tk()

window.geometry('600x700')
window.title('Check buttons')
window.resizable(0,1)

lbl = tk.Label(text = 'Choose an option:',
              padx = 5,
              pady = 5,
              fg = 'white', bg='green',
              )
lbl.grid(row=0, column=0, columnspan=2, sticky='w')

options = []
options_vars = []
for i in range(3):
    # create a Checkbutton
    options.append(tk.Checkbutton())
    # create a IntVar to store its status
    options_vars.append(tk.IntVar())
    options[-1].configure(text=f'Option {i+1}',
    # variable to store checkbutton status
    variable = options_vars[i],
    # values of variable depending on
    # whether checkbutton is marked or not
    # default values for onvalue and offvalue are (1) True, (0) False
    #onvalue=1,
    #offvalue=0
    )
    options[-1].grid(row=i+1, column=0, sticky='w')

    """def show_results():
        for index, value in enumerate(options_vars):
            if value.get():
                print(f'Option {index + 1} is marked.')"""

    def show_results():
        for index, value in enumerate(options_vars):
                if value.get():
                    print(f'Option {index + 1} has a value of: {value.get()}.')

tk.Button(text='Show results', command=show_results).grid(row=4, column=0)




window.mainloop()
