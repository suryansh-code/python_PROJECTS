import random
import tkinter as tk

window=tk.Tk()
window.title('its just an app')
window.geometry('400x300')


def name_generator():

    phrases='hlo','1231414','4124134','434343','122343','4134134','43443434','4343241'

    name=str(entry1.get())
    best=str(entry2.get())

    return phrases[random.randint(0,8)]+name+best

def name_display():
    greeting=name_generator()

    name_display = tk.Text(master=window,height=10 , width=30)
    name_display.grid(column=0,row=4)

    name_display.insert(tk.END,greeting)


label1=tk.Label(text='WELCOME TO MY APP \n PASSWORD GENERATOR')
label1.grid(column=1,row=0)

label2=tk.Label(text='whats your name')
label2.grid(column=0,row=1)

label3=tk.Label(text='what is the thing you cant forget')
label3.grid(column=0,row=2)

entry1=tk.Entry()
entry1.grid(column=1,row=1)

entry2=tk.Entry()
entry2.grid(column=1,row=2)


button1=tk.Button(text='click',bg='red',command=name_display)
button1.grid(column=0,row=3)

window.mainloop()
