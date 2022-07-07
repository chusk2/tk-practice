"""Create a pomodoro coundown counter"""
import tkinter as tk
import sys
import os

os.chdir('/home/daniel/code/tk/pomodoro')

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
TIME_SECONDS = WORK_MIN * 60

cycles = 1


def counter(time_seconds):
    """Creates the conversion from seconds to min and seconds
    Sets the time in the timer using the given timer colour"""
    global cycles
    # get the current time
    mins = time_seconds // 60
    if mins < 10 :
        mins = f'0{mins}'
    else:
        mins = str(mins)
    seconds = time_seconds % 60
    if seconds < 10:
        seconds = f'0{seconds}'
    else:
        seconds = str(seconds)
    current_time = f'{mins}:{seconds}'
    time_seconds -= 1
    # special form of accessing canvas widgetds
    canvas.itemconfig(timer_text, text=current_time)
    # exit when countdown is reached
    if current_time == '00:00':
        cycles += 1
        print(cycles)
        start_counter()
        
    else:
        # repeat the function every 1 second
        # using current mins and seconds
        window.after(1000, counter, time_seconds)

def start_counter():
    """Starts the counterback with WORK_MIN"""
    global cycles
    # work out the working time
    if cycles % 2 != 0 and cycles != 7:
        cycle_time = WORK_MIN * 60
        canvas.itemconfig(timer_text, fill='white')
        counter(cycle_time)

    # take a break for 5 min
    #TODO show label telling it's a break and duration
    elif cycles % 2 == 0:
        cycle_time = SHORT_BREAK_MIN * 60
        # number of working cycles: cycles // 2. Result must be integer
        tick_lbl.config(text = '\u2714' * (cycles // 2))
        canvas.itemconfig(timer_text, fill='green')
        counter(cycle_time)

    # take a big break of 20 min
    #TODO show label telling it's a break and duration
    elif cycles == 7:
        cycle_time = LONG_BREAK_MIN * 60
        canvas.itemconfig(timer_text, fill='blue')
        counter(cycle_time)

window = tk.Tk()
window.geometry('370x400')
window.config(padx=5, pady=5, bg=YELLOW)
window.resizable(0,0)
window.title("Pomodoro Counter")

# set app icon
#use .ico for windows systems
if sys.platform.startswith('win'):
    window.iconbitmap('tomato.ico')
else:
    logo = tk.PhotoImage(file='tomato.png')
    window.tk.call('wm', 'iconphoto', window._w, logo)
    #window.iconbitmap('tomato.xbm')

# title Timer
title = tk.Label(window, text='Timer',
    font=(FONT_NAME, 35, 'bold italic'),
    fg=GREEN, bg=YELLOW)
title.grid(row=0, column=1, pady=5, padx=5)

canvas = tk.Canvas(width=202, height=225, bg=YELLOW,
    highlightthickness=0)
# tomato.png 200x223
tomato_img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text='00:00', fill='white',
    font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1,column=1, pady=10)

# buttons
start_btn = tk.Button(window, text='Start',
    bg='white', fg='black', highlightthickness=0,
    command=start_counter)
start_btn.grid(row=2, column=0, padx=10, pady=5)

reset_btn = tk.Button(window, text='Reset',
    bg='white', fg='black', highlightthickness=0)
reset_btn.grid(row=2, column=2, padx=10, pady=5)

# tick label
tick_lbl = tk.Label(window, text='',
    font=(FONT_NAME, 25, 'bold'), fg=GREEN, bg=YELLOW)
tick_lbl.grid(row=3, column=1)


window.mainloop()
