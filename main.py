"""
Tkinter Based APRS String generator for JS8Call
KN4MKB, 2021
User can enter email/phonenumber, as well as a message to generate a string of text for JS8 Call
@author: ModernHam
"""
import tkinter
from tkinter import *
choice = ""
JS8Content = ""

def update_command():
    dest = dest_text.get()
    content = content_text.get()
    print(choice)

    if choice == "SMS":
        print("Computing SMS")
        JS8Content = "@APRSIS CMD :SMSGTE   :@" + dest + " " + content + "{04}"
    elif choice == "EMAIL":
        print("Computing EMAIL")
        JS8Content = "@APRSIS CMD :EMAIL-2  :" + dest + " " + content + "{03}"
    elif choice == "GRID":
        print("Computing GRID")
        JS8Content = "@APRSIS GRID " + content
    elif choice == "APRS":
        print("Computing APRS")
        JS8Content = "@APRSIS CMD :" + dest + " :" + content + "{05}"
    else:
        print("Default SMS")
        JS8Content = "@APRSIS CMD :SMSGTE   :@" + dest + " " + content + "{04}"
    TextOut.delete(END, "end")
    TextOut.delete('1.0', END)
    TextOut.insert(END, JS8Content)

def assign(option):
    global choice
    print(option)
    choice = option
    return

window = Tk()
window.wm_title("APRS CALL")
window.geometry("245x250")

#Labels for text Entry
l1 = Label(window, text="Mode:")
l1.grid(row=0, column=0)

l2 = Label(window, text="Destination:")
l2.grid(row=2, column=0)

l3 = Label(window, text="Content:")
l3.grid(row=4, column=0)

choices = ['SMS', 'EMAIL', 'GRID', 'APRS']
variable = StringVar(window)
variable.set('SMS')
w = OptionMenu(window, variable, *choices, command = assign)
w.grid(row=0, column=1)

dest_text=StringVar()
e2 = Entry(window, textvariable=dest_text)
e2.grid(row=2, column=1)

content_text=StringVar()
e3 = Entry(window, textvariable=content_text)
e3.grid(row=4, column=1, columnspan = 2)


#DisplayWidgets
l4 = Label(window, text="JS8 Text")
l4.grid(row=8, column=0, columnspan = 2, pady = 10)

TextOut = Text(window, height=5, width=30)
TextOut.grid(row=9, column=0,columnspan = 2, pady = 10)



#Create Buttons
b4 = Button(window, text="Generate", width=12, command=update_command)
b4.grid(row=7, column=0, columnspan = 2)
window.mainloop()