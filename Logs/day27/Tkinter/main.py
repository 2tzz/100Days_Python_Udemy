from tkinter import *


def button_clicked():
    print("I got clicked")
    my_label["text"] = whatever.get()


window = Tk()
window.minsize(width=500 , height=300)
window.config(padx=100,pady=100)


my_label = Label(text="I am a label" , font=("Arial",24 , ))
whatever = StringVar()
my_label.grid(column= 0 , row=0)



button = Button (text="click me" , command=button_clicked)
button.grid(column=1 , row=1)

new_button = Button (text="click me" , command=button_clicked)
new_button.grid(column=2 , row=0)


input = Entry(width=20 , textvariable=whatever)
input.grid(column=3,row=2)





 
























window.mainloop()