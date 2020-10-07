from tkinter import *

a=Tk()

def oye():
    label3=Label(text='hai hussain this is santosh')
    label3.grid(row=3,column=0)

def click():
    b=k.get()
    label3=Label(text=b)
    label3.grid(row=7,column=0)
k=StringVar()
a.title('this is santosh adda')

a.geometry('400x400+0+0')




label1=Label(text='I am santosh', fg='white', bg='blue', font=('arial',20,'italic'))
label1.grid(row=0,column=0)
label2=Label(text='I am hussain', fg='red', bg='yellow', font=('times',20,'bold'))
label2.grid(row=1,column=0)

but1=Button(text='say hi to hussain', fg='blue', bg='white',font=('roman',30,'underline'), command=oye)
but1.grid(row=2,column=0)

but2=Button(text='submit',fg='blue',bg='white', font=30, command=click)
but2.grid(row=5,column=0)

text1=Entry(textvariable=k,fg='blue', bg='white', font=12)
text1.grid(row=4,column=0)

menu=Menu()
list1=Menu()
list1.add_command(label='new')
list1.add_command(label='open')
list1.add_command(label='save')
list1.add_command(label='save as')

list2=Menu()
list2.add_command(label='undo')
list2.add_command(label='redo')

menu.add_cascade(label='file',menu=list1)
menu.add_cascade(label='Edit',menu=list2)
a.config(menu=menu)

a.mainloop()