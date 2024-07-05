#Calculator App
from tkinter import *
def button_press(num):
    global equ_text
    equ_text=equ_text+str(num)
    equ_label.set(equ_text)

def equal():
    global equ_text
    try:
        total=str(eval(equ_text))
        equ_label.set(total)
        equ_text=total
    except ZeroDivisionError:
        equ_label.set("ArithmeticError")
        equ_text=""
    except SyntaxError:
        equ_label.set("SyntaxError")
        equ_text=""
    

def clears():
    global equ_text
    equ_label.set("")
    equ_text=""


window=Tk()
window.title("Calculator App")
window.geometry("500x500")

equ_text=""
equ_label=StringVar()
label=Label(window,textvariable=equ_label,font=('consolas',20),bg="pink",width=24,height=2)
label.pack()

frame=Frame(window)
frame.pack()

button1=Button(frame,text=1,height=4,width=9,font=35,command=lambda:button_press(1))
button1.grid(row=0,column=0)

button2=Button(frame,text=2,height=4,width=9,font=35,command=lambda:button_press(2))
button2.grid(row=0,column=1)

button3=Button(frame,text=3,height=4,width=9,font=35,command=lambda:button_press(3))
button3.grid(row=0,column=2)

plus=Button(frame,text='+',height=4,width=9,font=35,command=lambda:button_press('+'))
plus.grid(row=0,column=3)

button4=Button(frame,text=4,height=4,width=9,font=35,command=lambda:button_press(4))
button4.grid(row=1,column=0)

button5=Button(frame,text=5,height=4,width=9,font=35,command=lambda:button_press(5))
button5.grid(row=1,column=1)

button6=Button(frame,text=6,height=4,width=9,font=35,command=lambda:button_press(6))
button6.grid(row=1,column=2)

diff=Button(frame,text='-',height=4,width=9,font=35,command=lambda:button_press('-'))
diff.grid(row=1,column=3)

button7=Button(frame,text=7,height=4,width=9,font=35,command=lambda:button_press(7))
button7.grid(row=2,column=0)

button8=Button(frame,text=8,height=4,width=9,font=35,command=lambda:button_press(8))
button8.grid(row=2,column=1)

button9=Button(frame,text=9,height=4,width=9,font=35,command=lambda:button_press(9))
button9.grid(row=2,column=2)

mul=Button(frame,text='*',height=4,width=9,font=35,command=lambda:button_press('*'))
mul.grid(row=2,column=3)

button0=Button(frame,text=0,height=4,width=9,font=35,command=lambda:button_press(0))
button0.grid(row=3,column=0)

decimal=Button(frame,text='.',height=4,width=9,font=35,command=lambda:button_press('.'))
decimal.grid(row=3,column=1)

equalbutton=Button(frame,text='=',height=4,width=9,font=35,command=equal)
equalbutton.grid(row=3,column=2)

div=Button(frame,text='/',height=4,width=9,font=35,command=lambda:button_press('/'))
div.grid(row=3,column=3)

clear=Button(window,text='clear',height=4,width=12,command=clears)
clear.pack()

window.mainloop()
