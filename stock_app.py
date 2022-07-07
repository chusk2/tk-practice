import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.geometry("390x600")
window.resizable(0,0)
window.title('Stock Manager')

inventory = []

# Labels
label_names = ['home', 'add_product','info']
# create 4 label widgets
label_objects = [tk.Label() for i in label_names]
# apply style to all labels
for label in label_objects:
    label.config(font=("Verdana", 30),
                fg="white",
                bg='green',
                justify='center',
                height=2)

labels = {k:v for k,v in zip(label_names, label_objects)}

# assign text values for all labelsexit()
labels['home'].config(text='Inventory')
labels['add_product'].config(text='Add a product item')
labels['info'].config(text='Database\nInformation')

# Frames
frame_objects = [tk.LabelFrame(window, borderwidth=1) for i in label_names]
frames = {k:v for k,v in zip(label_names, frame_objects)}

# Define behaviour for all menu items
def home():
    """Show home page content"""
    # remove previous widgets
    for k in labels.keys():
        labels[k].grid_forget()
    for frame in frame_objects:
        frame.grid_forget()
    # show own widgets
    labels['home'].grid(row=0, column=0, ipadx=15, sticky='we')
    frames['home'].grid(row=1, column=0, sticky='w', padx=5, pady=5)

    # Create treeview
    column_labels = ('id', 'Name', 'Price')
    table = ttk.Treeview(frames['home'], columns=column_labels, height=5)
    # hide column #0
    table.column('#0', width=0, minwidth=0, anchor='w')
    # set width and min width for each column
    table.column('id', width=40, minwidth=30, anchor='center')
    table.column('Name', width=150, minwidth=100, anchor='w')
    table.column('Price', width=80, minwidth=40, anchor='e')
    # create headings
    for lbl in column_labels:
        table.heading(lbl, text=lbl, anchor='w')  
    # insert products in table
    for index, prod in enumerate(inventory):
        data = [index, *prod.values()]
        table.insert(parent='', index=tk.END, values=data)
    # show table
    table.grid(row=0, column=0)

def add_product():
    """Form to add a product to database"""
    # remove previous widgets
    for k in labels.keys():
        labels[k].grid_forget()
    for frame in frame_objects:
        frame.grid_forget()
    # show own widgets
    labels['add_product'].grid(row=0, column=0, sticky='we')
    frames['add_product'].grid(row=1, column=0, sticky='we', padx=5, pady=5)
    # create form to add products

    # add product variables and button function
    prod_name = tk.StringVar()
    prod_price = tk.DoubleVar()
    prod_price.set(0)

    # product name
    product_name = tk.Label(frames['add_product'], text='Name')
    product_name.grid(row=0, column=0, sticky='nw', padx=5, pady=5)
    product_name_entry = tk.Entry(frames['add_product'],
        width=20, textvariable=prod_name)
    product_name_entry.grid(row=0, column=1, sticky='nw', padx=5, pady=5)

    # product price
    product_price = tk.Label(frames['add_product'], text='Price')
    product_price.grid(row=1, column=0, sticky='nw', padx=5, pady=5)
    product_price_entry = tk.Entry(frames['add_product'],
        width=10, textvariable=prod_price)
    product_price_entry.grid(row=1, column=1, sticky='nw', padx=5, pady=5)

    # product description
    product_description = tk.Label(frames['add_product'], text='Description')
    product_description.grid(row=2, column=0, sticky='nw', padx=5, pady=5)
    product_description = tk.Text(frames['add_product'],
        height=5,
        width=40,)
    product_description.grid(row=2, column=1, sticky='nw', padx=5, pady=5)

    # Buttons
    frame_buttons = tk.Frame(frames['add_product'])
    frame_buttons.grid(row=3, column=1, sticky='ne', padx=5, pady=5)

    # reset fields
    def empty_form():
        prod_name.set('')
        prod_price.set(0)
        product_description.delete('1.0', tk.END)

    # save product button
    def add():
        name = prod_name.get()
        price = prod_price.get()
        description = product_description.get('1.0', tk.END)
        prod_dict = {'name': name, 'price': price, 'description': description}
        # check if all three fields are filled
        if all(prod_dict.values()):
            inventory.append(prod_dict)
            empty_form()
            print(inventory)
        else:
            for k,v in prod_dict.items():
                if not v:
                    messagebox.showerror('Missing information',
                        f'The product {k} is missing')

    save_button = tk.Button(frame_buttons, text='Add product',command=add)
    save_button.grid(row=0, column=0, sticky='ne', padx=5, pady=5)

    empty_button = tk.Button(frame_buttons, text='Empty form',
        command=empty_form)
    empty_button.grid(row=0, column=1, sticky='ne', padx=5, pady=5)


def info():
    """Show information page content"""
    # remove previous widgets
    for k in labels.keys():
        labels[k].grid_forget()
    for frame in frame_objects:
        frame.grid_forget()
    # show own widgets
    labels['info'].grid(row=0, column=0, sticky='we')
    frames['info'].grid(row=1, column=0, sticky='we', padx=5, pady=5)

    inventory_content = f'The database stores currently {len(inventory)} items'
    inventory_lbl = tk.Label(frames['info'], text=inventory_content,
        font=('Courier', 12))
    inventory_lbl.grid(row=0, column=0)


def exit_program():
    """Quit the application"""
    window.destroy()

# Create an upper menu
upper_menu = tk.Menu(window)
upper_menu.add_command(label='Inicio', command=home)
upper_menu.add_command(label='Add product', command=add_product)
upper_menu.add_command(label='Database info', command=info)
upper_menu.add_command(label='Exit', command=exit_program)
# assign upper menu to window
window.config(menu=upper_menu)
home()
print(window.winfo_geometry())
window.mainloop()
