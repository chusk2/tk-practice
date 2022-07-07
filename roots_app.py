import tkinter as tk
import sympy


class Equation:
    def __init__(self):
        self.coefficients = []

    def add_coefficient(self, num):
        self.coefficients.append(num)

    def solve(self):
        a, b, c = self.coefficients
        x = sympy.Symbol('x', real=True)
        solutions = sympy.solve(a * x ** 2 + b * x + c)

        if solutions:
            if len(solutions) == 1:
                sols = f'{solutions[0]}'
            else:
                sols = f'{solutions[0]} , {solutions[1]}'

            return 'Raices: {' + sols + '}'
        else:
            return 'Discriminante negativo. Sin solución...'

    def eq_expression(self):
        # add coefficient with its sign
        terms = []
        for index, value  in enumerate(self.coefficients):
            # negative
            if value < 0 and value != -1:
                terms.append(f'{value}')
            # positive
            elif value > 0 and value != 1:
                terms.append(f'+{value}')
            # +1x²
            elif value == 1 and index == 0:
                terms.append('')
            # -1x²
            elif value == -1 and index == 0:
                terms.append('-')
            # +1x
            elif value == 1 and index != 0:
                terms.append('+')
            # -1x
            elif value == -1 and index != 0:
                terms.append('-')
            else : # term is null
                terms.append(0)
        # define literal parts
        literal_terms = ['x^2', 'x', '']

        # combine all parts together
        equation_expression = ''
        for index, value in enumerate(terms):
            if value != 0:  # make sure to append only if the term is not null
                equation_expression += f'{value}{literal_terms[index]}'
        return equation_expression


class App:

    def __init__(self):
        self.app = tk.Tk()
        self.app.geometry("600x250")
        self.app.title('Ecuación 2do grado')

        # introduction label
        self.title = tk.Label(text='Introduce los coeficientes de la ecuación de 2do grado:',
                              font=("Sans Serif", 12),
                              padx=15, pady=15,
                              anchor=tk.CENTER
                              )
        self.title.grid(row=0, column=0)

        # create a frame for coefficients
        self.frame = tk.Frame(self.app, borderwidth=2, width=30)
        self.frame.grid(column=0, row=1, sticky='w', padx=15, pady=20)
        # ask for coefficients
        self.input_label = tk.Label(self.frame, text=f'Coeficiente a:')
        self.input_label.grid(row=0, column=0, sticky='w')
        # entry label for coefficient
        self.entry = tk.Entry(self.frame, width=10)
        self.entry.grid(row=0, column=1, sticky='e', padx=10)
        # https://www.pythontutorial.net/tkinter/tkinter-event-binding/
        self.entry.bind('<Return>', self.process_entry)
        # when coefficients are wrong
        self.label_warning = tk.Label(self.frame, text='')

        # show the result
        self.label_results = tk.Label(self.frame, text='')
        self.label_results.grid(row=2, column=0)
        # reset
        self.button_reset = tk.Button(self.frame, text='Reset', command=self.reset)
        self.button_reset.grid(row=1, column=0, sticky='w', pady=15)

        self.equation = Equation()

        self.app.mainloop()

    def process_entry(self, event=None):

        # set the label for the current coefficient
        coeff = self.entry.get()
        # convert value to integer
        try:
            self.equation.add_coefficient(int(coeff))
            self.clean_entry()
            # figure out which coefficient ask for
            if len(self.equation.coefficients) == 1:
                letter = 'b'
                self.input_label.config(text=f'Coeficiente {letter}:')

            elif len(self.equation.coefficients) == 2:
                letter = 'c'
                self.input_label.config(text=f'Coeficiente {letter}:')

            else:
                a, b, c = self.equation.coefficients
                result = f'Solución de la ecuación: {self.equation.eq_expression()} = 0'
                result += f'\n{self.equation.solve()}'

                self.label_results.config(text=result)
                self.input_label.grid_remove()
                self.entry.grid_remove()

        except ValueError:
            # show warning and clear entry widget
            self.label_warning.configure(text='Los coeficientes introducidos no son válidos.\n¡Solo valores numéricos!')
            self.label_warning.grid(row=3, column=0)
            self.entry.delete(0, 'end')

    def solve_equation(self):
        results = self.equation.solve()
        self.label_results.configure(text=results)

    def clean_entry(self):
        self.entry.delete(0, 'end')

    def reset(self):
        self.input_label.config(text=f'Coeficiente a:')
        self.input_label.grid(row=1, column=0)
        self.entry.grid(row=1, column=1)
        self.label_results.configure(text='')
        self.equation = Equation()


window = App()
