from tkinter import *


def button_clicked():
    print("I got clicked")

    miles = int(whatever.get()) / 1.0

    km = miles * 1.6

    calculation["text"] = km


window = Tk()
window.minsize(width=500 , height=300)
window.config(padx=100,pady=100)

whatever = StringVar()
cal_out = 0


input = Entry(width=20 , textvariable= whatever)
input.grid(column=1,row=0)


miles = Label(text="Miles" , font=("Arial",24 , ))
miles.grid(column= 2 , row=0)

equal = Label(text="is equal to" , font=("Arial",24 , ))
equal.grid(column= 0 , row=1)

calculation = Label(text= cal_out , font=("Arial",24 , ))
calculation.grid(column= 1 , row=1)

km = Label(text="Km" , font=("Arial",24 , ))
km.grid(column= 2 , row=1)

button = Button (text="calculate" , command=button_clicked)
button.grid(column=1 , row=2)



window.mainloop()