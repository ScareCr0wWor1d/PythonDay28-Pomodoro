import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

my_window = tkinter.Tk()
my_window.title('Pomodoro Timer')
my_window.wm_minsize(500,500)

title_lbl = tkinter.Label(text='POMODORO',font=('System', 10))
title_lbl.grid(column=1, row=0)

start_btn = tkinter.Button(text='Start')
start_btn.grid(column=0, row=2)

reset_btn = tkinter.Button(text='Reset')
reset_btn.grid(column=2, row=2)

my_window.mainloop()
