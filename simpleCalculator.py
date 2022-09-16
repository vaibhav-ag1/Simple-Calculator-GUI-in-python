from bisect import bisect_right
from tkinter import *

root=Tk()

def erase():
    e.delete(0,END)
def clicked(data):
    e.insert(END,data)

def adder():
    y=e.get()
    if(y[-1]!='+'):
        e.insert(END,"+")

def equal():
    x=list(e.get().split("+"))
    sum=0
    for i in x:
        sum =sum+int(i)
    e.delete(0,END)
    e.insert(0,sum)
    

e=Entry(root,borderwidth=5,width=28)
e.grid(row=0,columnspan=3)

button9=Button(root,text="9",padx=20,pady=20,command=lambda:clicked(9))
button9.grid(row=1,column=0)

button8=Button(root,text="8",padx=20,pady=20,command=lambda:clicked(8))
button8.grid(row=1,column=1)

button7=Button(root,text="7",padx=20,pady=20,command=lambda:clicked(7))
button7.grid(row=1,column=2)

button6=Button(root,text="6",padx=20,pady=20,command=lambda:clicked(6))
button6.grid(row=2,column=0)


button5=Button(root,text="5",padx=20,pady=20,command=lambda:clicked(5))
button5.grid(row=2,column=1)

button4=Button(root,text="4",padx=20,pady=20,command=lambda:clicked(4))
button4.grid(row=2,column=2)

button3=Button(root,text="3",padx=20,pady=20,command=lambda:clicked(3))
button3.grid(row=3,column=0)

button2=Button(root,text="2",padx=20,pady=20,command=lambda:clicked(2))
button2.grid(row=3,column=1)

button1=Button(root,text="1",padx=20,pady=20,command=lambda:clicked(1))
button1.grid(row=3,column=2)

button0=Button(root,text="0",padx=20,pady=20,command=lambda:clicked(0))
button0.grid(row=4,column=0)

clear=Button(root,text="CLEAR",padx=36,pady=20,command=erase)
clear.grid(row=4,column=1,columnspan=2)

plus=Button(root,text="+",padx=19,pady=20,command=adder)
plus.grid(row=5,column=0)

eqSign=Button(root,text="=",padx=49,pady=20,command=equal)
eqSign.grid(row=5,column=1,columnspan=2)


root.mainloop()