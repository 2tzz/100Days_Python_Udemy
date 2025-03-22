from tkinter import *
import math


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
def start_timer() :
    countdown(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10 :
        count_sec = f"0{count_sec}"
    

    canvas.itemconfig(timer_text , text=f"{count_min}:{count_sec}")
    if count > 0 :
        window.after(1000, countdown ,count - 1)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomadoro")
window.config(padx=100, pady=100 , bg=GREEN)



timer = Label(text="Timer" , bg=GREEN ,  fg=YELLOW , font=(FONT_NAME,50,"bold"))
timer.grid(column=1 , row=0)


canvas = Canvas(width=200 , height= 224 , bg=GREEN, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112 , image=tomato_image)
timer_text = canvas.create_text(102 , 135 , text='00:00' , fill="white" , font=(FONT_NAME,35,"bold"))
canvas.grid(column=1 , row=1 ) 



start_button = Button(text="Sart",font=(FONT_NAME,10,"bold") ,width=8, height=1, background=YELLOW ,border=OFF, command=start_timer )
start_button.grid(column=0 , row=2)

reset_button = Button(text="Reset",font=(FONT_NAME,10,"bold") ,width=8, height=1 ,bg=YELLOW ,border=OFF, command=start_timer)
reset_button.grid(column=2 , row=2)

tick = Label(text="✔" , bg=GREEN ,  fg=YELLOW , font=(FONT_NAME,20,"bold"))
tick.grid(column=1 , row=3)






window.mainloop()