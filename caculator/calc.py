from tkinter import*
from tkinter import messagebox

a=Tk()

def hi():
    lab3 = Label(text="by hussainsha", fg="white", bg="blue")
    lab3.grid(row=0, column=0, sticky='w')
def hello():
    lab4 = Label(text="by reshma parveen", fg="white", bg="blue")
    lab4.grid(row=0, column=0, sticky='w')

def click():
    b=z.get()
    lab5=Label(text=b, fg='white', bg='blue')
    lab5.grid(row=7, column=0)
def qfile():
    m=messagebox.askyesno(title='Quit',message='Are you sure you want to Quit')
    if m==1:
        a.destroy()
z=StringVar()

a.title("my first panel")
a.geometry("500x500+0+0")
lab1=Label(text="hi darling i l u", fg="white", bg="blue")
lab1.grid(row=0,column=0,sticky='w')

lab2=Label(text="ya darling i 2 l u", fg="green", bg="yellow")
lab2.grid(row=1, column=0)

but1=Button(text='hi baby', fg='white', bg='blue',command=hi)
but1.grid(row=2,column=0)
but2=Button(text='ya baby', fg='green', bg='yellow',command=hello)
but2.grid(row=3,column=0)
but3=Button(text='click', fg='green', bg='yellow',command=click)
but3.grid(row=5,column=0)

textbox=Entry(textvariable=z)
textbox.grid(row=6, column=0)

mymenu=Menu()

listone=Menu()
listone.add_command(label='new file')
listone.add_command(label='open file')
listone.add_command(label='save file')
listone.add_command(label='quit',command=qfile)

listtwo=Menu()
listtwo.add_command(label='undo')
listtwo.add_command(label='redo')


mymenu.add_cascade(label='File', menu=listone)
mymenu.add_cascade(label='Edit',menu=listtwo)


a.config(menu=mymenu)
a.mainloop()



'''widget = Label(None, text="its time die")
widget.pack()
widget.mainloop()'''
