from  tkinter import *
from tkinter import colorchooser, filedialog

z=Tk()

def ofile():
    file=filedialog.askopenfile()
    '''lab1=Label(text=file).pack()'''
    file1=file.name
    file2=open(file1)
    lab2=Label(text=file2.read()).pack()


def ccolor():
    color=colorchooser.askcolor()
    lab=Label(text='your selected color',bg=color[1]).pack()
z.title('colors')
z.geometry("1000x1000+190+100")


but=Button(text='select color',width=30,command=ccolor).pack()
but1=Button(text='open', width=60, command=ofile).pack()

z.mainloop()