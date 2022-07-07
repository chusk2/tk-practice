"""Crear menu"""
import tkinter as tk

window = tk.Tk()
window.geometry('500x500')
window.resizable(0,1)

main_menu = tk.Menu()
menu_options = ['Archivo',
                'Editar',
                'Selección',
                'Ver',
                'Ir',
                'Ejecutar',
                'Terminal',
                'Ayuda']

archivo_options = ['Nuevo archivo de texto',
                  'Nuevo archivo...',
                  'Nueva carpeta',
                  'Abrir archivo...',
                  'Abrir carpeta...',
                  ]

# menu archivo
archivo_menu = tk.Menu(main_menu, tearoff=0)

for i in archivo_options[:3]:
    archivo_menu.add_command(label=i)

archivo_menu.add_separator()

for i in archivo_options[3:]:
    archivo_menu.add_command(label=i)

archivo_menu.add_command(label='Salir', command=window.quit)

# populate main menu
main_menu.add_cascade(label='Archivo', menu=archivo_menu)

for i in menu_options[1:]:
    main_menu.add_command(label=i)

close = tk.Button(text='Cerrar',
                 command = window.destroy)
close.pack()

window.config(menu=main_menu)

window.mainloop()
