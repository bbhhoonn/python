from tkinter import *

def button_press(num):
    global equation_text
    try:
        equation_text=equation_text+str(num)
        equation_lable.set(equation_text)
    except TypeError:
        equation_lable.set('type error')
        equation_text=""
        
def equals():
    global equation_text
    try:
        total=eval(equation_text)
        equation_lable.set(total)
        equation_text=total
    except SyntaxError:
        equation_lable.set("syntax error")
        equation_text=""
    except ZeroDivisionError:
        equation_lable.set("arithmetc error")
        equation_text=""
        
def clear():
    global equation_text
    equation_lable.set("")
    equation_text=""

window=Tk()
window.title("계산기")
window.geometry("500x500")

equation_text=""
equation_lable=StringVar()
lable=Label(window, textvariable=equation_lable, font='consolas', bg='white', width=24, height=2)
lable.pack()

frame=Frame(window)
frame.pack()

button1=Button(frame, text=1, width=9, height=4, font=35, command= lambda : button_press(1))
button1.grid(row=0,column=0)

button2=Button(frame, text=2, width=9, height=4, font=35, command= lambda : button_press(2))
button2.grid(row=0,column=1)

button3=Button(frame, text=3, width=9, height=4, font=35, command= lambda : button_press(3))
button3.grid(row=0,column=2)

button4=Button(frame, text=4, width=9, height=4, font=35, command= lambda : button_press(4))
button4.grid(row=1,column=0)

button5=Button(frame, text=5, width=9, height=4, font=35, command= lambda : button_press(5))
button5.grid(row=1,column=1)

button6=Button(frame, text=6, width=9, height=4, font=35, command= lambda : button_press(6))
button6.grid(row=1,column=2)

button7=Button(frame, text=7, width=9, height=4, font=35, command= lambda : button_press(7))
button7.grid(row=2,column=0)

button8=Button(frame, text=8, width=9, height=4, font=35, command= lambda : button_press(8))
button8.grid(row=2,column=1)

button9=Button(frame, text=9, width=9, height=4, font=35, command= lambda : button_press(9))
button9.grid(row=2,column=2)

button0=Button(frame, text=0, width=9, height=4, font=35, command= lambda : button_press(0))
button0.grid(row=3,column=0)

plus=Button(frame, text="+", width=9, height=4, font=35, command= lambda : button_press("+"))
plus.grid(row=0,column=3)

minus=Button(frame, text="-", width=9, height=4, font=35, command= lambda : button_press("-"))
minus.grid(row=1,column=3)

multiply=Button(frame, text="*", width=9, height=4, font=35, command= lambda : button_press("*"))
multiply.grid(row=2,column=3)

divide=Button(frame, text="/", width=9, height=4, font=35, command= lambda : button_press("/"))
divide.grid(row=3,column=3)

equal=Button(frame, text="=", width=9, height=4, font=35, command= lambda : equals())
equal.grid(row=3,column=2)

decimal=Button(frame, text=".", width=9, height=4, font=35, command= lambda : button_press("."))
decimal.grid(row=3,column=1)

clear=Button(frame, text='clear', height=2, font=35, command= lambda : clear())
clear.grid(row=4,column=0,columnspan=4,sticky=E+W)

window.mainloop()