from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
st_ticks = ""
# ---------------------------- TIMER RESET ------------------------------- #



def reset_timer():
    window.after_cancel(timer)
    label.config(text= "Timer")
    canvas.itemconfig(timer_text, text = "00:00")
    check_mark.config(text=" ")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 2 == 0:
        count_down(short_break)
        label.config(text="Break", fg=RED)
    elif reps % 8 == 0:
        count_down(long_break)
        label.config(text="Rest", fg=PINK)
    else:
        count_down(work_min)
        label.config(text="Timer", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global st_ticks
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer = window.after(1000, count_down, count - 1) # Args Take Function Parameter
    else:
        start_timer()

        work_session = math.floor(reps/2)
        for _ in range(work_session):
            st_ticks += "✓"
        check_mark.config(text= st_ticks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady= 50 , bg= YELLOW )




label = Label(text="TIMER"  , fg= GREEN , bg= YELLOW, font=(FONT_NAME , 50))
label.grid(column=1,row=0)

button_start = Button(text="START" ,highlightthickness=0,command=start_timer)
button_start.grid(column=0 , row =  2)
button_reset = Button(text= "RESET" ,highlightthickness=0,command=reset_timer)
button_reset.grid(column=2, row = 2)


check_mark = Label(text= st_ticks, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25))
check_mark.grid(column=1, row=2)




canvas = Canvas(width=200 , height=230 , bg= YELLOW , highlightthickness= 0 )
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 115, image= image )
timer_text = canvas.create_text(103, 120, text= "00:00", fill="white", font=(FONT_NAME , 35, "bold"))
canvas.grid(column=1 , row= 1)






window.mainloop()