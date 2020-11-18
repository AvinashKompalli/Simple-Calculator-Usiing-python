enter=""
def press(num):  
    global enter
    enter = enter + str(num) 
    eq.set(enter) 

def clear():
    global enter
    enter = "" 
    eq.set("") 

def equal():
    global enter
    total = str(eval(enter)) 
    eq.set(total) 
    enter=total
    
     
from tkinter import *
calc=Tk()
eq=StringVar()
calc.title("Calculator")
calc.configure(background="Black")
entry=Entry(calc, textvariable=eq)
entry.grid(columnspan=4,ipadx=70)



b1 = Button(calc, text=' 1 ',command=lambda: press(1), height=2, width=10) 
b1.grid(row=2, column=0) 

b2 = Button(calc, text=' 2 ', command=lambda: press(2), height=2, width=10) 
b2.grid(row=2, column=1) 

b3 = Button(calc, text=' 3 ', command=lambda: press(3), height=2, width=10) 
b3.grid(row=2, column=2) 

b4 = Button(calc, text=' 4 ', command=lambda: press(4), height=2, width=10) 
b4.grid(row=3, column=0) 

b5 = Button(calc, text=' 5 ', command=lambda: press(5), height=2, width=10) 
b5.grid(row=3, column=1) 

b6 = Button(calc, text=' 6 ', command=lambda: press(6), height=2, width=10) 
b6.grid(row=3, column=2) 

b7 = Button(calc, text=' 7 ', command=lambda: press(7), height=2, width=10) 
b7.grid(row=4, column=0) 

b8 = Button(calc, text=' 8 ', command=lambda: press(8), height=2, width=10) 
b8.grid(row=4, column=1) 

b9 = Button(calc, text=' 9 ', command=lambda: press(9), height=2, width=10) 
b9.grid(row=4, column=2) 

b0 = Button(calc, text=' 0 ', command=lambda: press(0), height=2, width=10) 
b0.grid(row=5, column=1) 

plus = Button(calc, text=' + ', command=lambda: press("+"), height=2, width=10) 
plus.grid(row=2, column=3) 

minus = Button(calc, text=' - ', command=lambda: press("-"), height=2, width=10) 
minus.grid(row=3, column=3) 

multiply = Button(calc, text=' * ', command=lambda: press("*"), height=2, width=10) 
multiply.grid(row=4, column=3) 

divide = Button(calc, text=' / ', command=lambda: press("/"), height=2, width=10) 
divide.grid(row=5, column=3) 

modulus = Button(calc, text='%',command=lambda: press("%"), height=2, width=10)
modulus.grid(row=5,column=2)

value = Button(calc, text=' = ', command=equal, height=2, width=20) 
value.grid(row=6, column=2, columnspan=2) 

clear = Button(calc, text='Clear', command=clear, height=2, width=20) 
clear.grid(row=6, column=0,columnspan=2) 

Decimal= Button(calc, text='.', command=lambda: press('.'), height=2, width=10) 
Decimal.grid(row=5, column=0)
calc.mainloop()
