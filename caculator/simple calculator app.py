from tkinter import *

cal=Tk()

cal.title("Simple Calc for Primary School Child")

cal.geometry("700x500+100+100")

melabel = Label(text="Designed by DXC middileware Team",fg= 'Blue', bg='White',font=("Times",20,'bold'))
melabel.pack(side=TOP)
cal.config(background='Dark green')

textin=StringVar()
operator=""

def click(number):   #lambda:clickbut(1)
     global operator
     operator=operator+str(number)
     textin.set(operator)

def result():
     global operator
     add=str(eval(operator))
     textin.set(add)
     operator=''
def result():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''
def result():
     global operator
     mul=str(eval(operator))
     textin.set(mul)
     operator=''
def result():
     global operator
     div=str(eval(operator))
     textin.set(div)
     operator=''


def clrbut():
    textin.set('')


resultbox = Entry(textvar=textin,width=26, font=44)
resultbox.place(x=50, y=70)
b1=Button(text='0', width=7,bg='blue',fg='white',font=18,command=lambda:click(0))
b1.place(x=50,y=100)

b2=Button(text='1', width=7,bg='blue',fg='white',font=18,command=lambda:click(1))
b2.place(x=150,y=100)

b3=Button(text='2', width=7,bg='blue',fg='white',font=18,command=lambda:click(2))
b3.place(x=250,y=100)

b4=Button(text='3', width=7,bg='blue',fg='white',font=18,command=lambda:click(3))
b4.place(x=50,y=150)

b5=Button(text='4', width=7,bg='blue',fg='white',font=18,command=lambda:click(4))
b5.place(x=150,y=150)

b6=Button(text='5', width=7,bg='blue',fg='white',font=18,command=lambda:click(5))
b6.place(x=250,y=150)

b7=Button(text='6', width=7,bg='blue',fg='white',font=18,command=lambda:click(6))
b7.place(x=50,y=200)

b8=Button(text='7', width=7,bg='blue',fg='white',font=18,command=lambda:click(7))
b8.place(x=150,y=200)

b9=Button(text='8', width=7,bg='blue',fg='white',font=18,command=lambda:click(8))
b9.place(x=250,y=200)


b10=Button(text='9', width=7,bg='blue',fg='white',font=18,command=lambda:click(9))
b10.place(x=50,y=250)

b11=Button(text='+', width=7,bg='blue',fg='white',font=18,command=lambda:click('+'))
b11.place(x=150,y=250)

b12=Button(text='-', width=7,bg='blue',fg='white',font=18,command=lambda:click('-'))
b12.place(x=250,y=250)


b13=Button(text='.', width=7,bg='blue',fg='white',font=18,command=lambda:click('.'))
b13.place(x=50,y=300)

b14=Button(text='/', width=7,bg='blue',fg='white',font=18,command=lambda:click('/'))
b14.place(x=150,y=300)

b15=Button(text='*', width=7,bg='blue',fg='white',font=18,command=lambda:click('*'))
b15.place(x=250,y=300)

b16=Button(text='result', width=7,bg='blue',fg='white',font=18,command=result)
b16.place(x=50,y=350)

b17=Button(text='clr', width=7,bg='blue',fg='white',font=18,command=clrbut)
b17.place(x=150,y=350)


cal.mainloop()