import tkinter
from PIL import ImageTk, Image

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
Rep = 0
check = 0
timer = ''
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global Rep, check
    my_window.after_cancel(timer)
    Rep = 0
    check = 0
    canvas_tom.itemconfig(canvas_lbl, text="25:00")
    status_lbl.config(text='Wait to Start')
    checked_lbl.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global Rep, check
    Rep = Rep + 1
    if Rep == 1 or Rep == 3 or Rep == 5 or Rep == 7:
        checked_lbl.config(text=check*'✓' + '⧖')
        my_window.attributes('-topmost', True)
        status_lbl.config(text='Work', fg=GREEN)
        count_down(WORK_MIN)
        check += 1
        my_window.attributes('-topmost', False)
    elif Rep == 2 or Rep == 4 or Rep == 6:
        my_window.attributes('-topmost', True)
        checked_lbl.config(text=check * '✓')
        count_down(SHORT_BREAK_MIN)
        status_lbl.config(text='Short Break', fg=PINK)
        my_window.attributes('-topmost', False)
    elif Rep == 8:
        checked_lbl.config(text=check * '✓')
        my_window.attributes('-topmost', True)
        count_down(LONG_BREAK_MIN * 60)
        status_lbl.config(text='Long Break', fg=RED)
        my_window.attributes('-topmost', False)
    else:
        my_window.attributes('-topmost', True)
        canvas_tom.itemconfig(canvas_lbl, text="25:00")
        status_lbl.config(text='Cycle over', fg=GREEN)
        my_window.attributes('-topmost', False)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = int(count/60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count > 0:
        global timer
        timer = my_window.after(1000, count_down, count-1)
        canvas_tom.itemconfig(canvas_lbl, text=f"{count_min}:{count_sec}")
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

my_window = tkinter.Tk()
my_window.title('Pomodoro Timer')
my_window.config(pady=30, padx=50, bg=YELLOW)

title_lbl = tkinter.Label(text='PoMoDoRo', font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
title_lbl.grid(column=1, row=0)

canvas_tom = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas_tom.create_image(100, 112, image=tomato_img)

canvas_lbl = canvas_tom.create_text(100, 130, text='25:00', fill='white', font=('System', 20))
canvas_tom.grid(column=1, row=1)

start_btn = tkinter.Button(text='Start', width=10, height=2, highlightthickness=0, bg=YELLOW, fg=RED, command=start_timer)
start_btn.grid(column=0, row=2)

status_lbl = tkinter.Label(text='Wait to Start', font=(FONT_NAME, 20, 'bold'), bg=YELLOW, fg=GREEN)
status_lbl.grid(column=1, row=2)

checked_lbl = tkinter.Label(text='', font=(FONT_NAME, 20, 'bold'), bg=YELLOW, fg=GREEN)
checked_lbl.grid(column=1, row=3)

reset_btn = tkinter.Button(text='Reset', width=10, height=2, highlightthickness=0, bg=YELLOW, fg=RED, command=reset_timer)
reset_btn.grid(column=2, row=2)

my_window.mainloop()
