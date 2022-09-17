from tkinter import *

root=Tk()


e=Entry(root,borderwidth=5,width=45)
e.grid(row=0,columnspan=3)


def erase():
    e.delete(0,END)

def clicked(data):
    e.insert(END,data)

def add():
    global first_num
    global math
    first_num = int(e.get())
    math="add"
    e.delete(0,END)

def minus():
    global first_num
    global math
    first_num =int(e.get())
    math="minus"
    e.delete(0,END)

def multiply():
    global first_num
    global math
    first_num =int(e.get())
    math="multiply"
    e.delete(0,END)

def divide():
    global first_num
    global math
    first_num =int(e.get())
    math="divide"
    e.delete(0,END)

def equal():
    second_num = int(e.get())
    e.delete(0,END)
    
    if(math=="add"):
        ans =first_num+second_num
    
    if(math=="minus"):
        ans =first_num-second_num

    if(math=="multiply"):
        ans =first_num*second_num

    if(math=="divide"):
        ans=first_num/second_num

    e.insert(0,ans)
    

button9=Button(root,text="9",padx=40,pady=40,command=lambda:clicked(9))
button9.grid(row=1,column=0)

button8=Button(root,text="8",padx=40,pady=40,command=lambda:clicked(8))
button8.grid(row=1,column=1)

button7=Button(root,text="7",padx=40,pady=40,command=lambda:clicked(7))
button7.grid(row=1,column=2)

button6=Button(root,text="6",padx=40,pady=40,command=lambda:clicked(6))
button6.grid(row=2,column=0)


button5=Button(root,text="5",padx=40,pady=40,command=lambda:clicked(5))
button5.grid(row=2,column=1)

button4=Button(root,text="4",padx=40,pady=40,command=lambda:clicked(4))
button4.grid(row=2,column=2)

button3=Button(root,text="3",padx=40,pady=40,command=lambda:clicked(3))
button3.grid(row=3,column=0)

button2=Button(root,text="2",padx=40,pady=40,command=lambda:clicked(2))
button2.grid(row=3,column=1)

button1=Button(root,text="1",padx=40,pady=40,command=lambda:clicked(1))
button1.grid(row=3,column=2)

button0=Button(root,text="0",padx=40,pady=40,command=lambda:clicked(0))
button0.grid(row=4,column=0)

plus=Button(root,text="+",padx=39,pady=40,command=add)
plus.grid(row=4,column=1)

minus=Button(root,text="-",padx=40,pady=40,command=minus)
minus.grid(row=4,column=2)

clear=Button(root,text="CLEAR",padx=76,pady=40,command=erase)
clear.grid(row=5,column=1,columnspan=2)

multi=Button(root,text="X",padx=39,pady=40,command=multiply)
multi.grid(row=5,column=0)

division=Button(root,text="/",padx=40,pady=40,command=divide)
division.grid(row=6,column=0)

eqSign=Button(root,text="=",padx=90,pady=40,command=equal)
eqSign.grid(row=6,column=1,columnspan=2)


root.mainloop()