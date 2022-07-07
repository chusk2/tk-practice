import tkinter as tk

app = tk.Tk()
app.geometry("400x400")

label = tk.Label(text='Text goes here...')
label.pack()


def event_(event):
    label.config(text=entry.get())


entry = tk.Entry(width=10)
entry.pack()
entry.bind('<Return>', event_)

app.mainloop()