import tkinter as tk

window = tk.Tk()

content = tk.StringVar()
entry_ = tk.Entry(width=10, textvariable=content)
entry_.pack()

btn = tk.Button(text='Show entry content',
                # set label text to content of the entry label
                command=lambda : lbl.configure(text = content.get())
                )
btn.pack()

lbl = tk.Label()
lbl.pack()

window.mainloop()