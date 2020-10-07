from tkinter import *
from tkinter.constants import W, LEFT

z=Tk()
z.title("radio buttons")
z.geometry("700x700+100+0")

def select():
    a=v.get()
    if a==1:
        a1=Tk()
        a1.title("Python")
        a1.geometry("500x500")
        lab1=Label(a1,text='welcome to python programming').pack()
    elif a==2:
        a1 = Tk()
        a1.title("Java")
        a1.geometry("500x500")
        lab1 = Label(a1,text='welcome to java programming').pack()
    elif a==3:
        a1 = Tk()
        a1.title("Perl")
        a1.geometry("500x500")
        lab1 = Label(a1, text='welcome to perl programming').pack()
    elif a==4:
        a1 = Tk()
        a1.title("Ruby")
        a1.geometry("500x500")
        lab1 = Label(a1, text='welcome to Ruby programming').pack()



v=IntVar()
v.set(3)
list=[('python',1),('java',2),('perl',3),('ruby',4)]
lab=Label(text='choose programming \n language',justify=LEFT).pack()
'''Radiobutton(text='python',padx=40,variable=v,value=1,command=select).pack(anchor=W)
Radiobutton(text='Java',padx=40,variable=v,value=2,command=select).pack(anchor=W)
Radiobutton(text='perl',padx=40,variable=v,value=3,command=select).pack(anchor=W)
Radiobutton(text='Ruby',padx=40,variable=v,value=4,command=select).pack(anchor=W)... '''

for txt, val in list:
    Radiobutton(z,text=txt,padx=40,indicatoron=0, width=30,variable=v,command=select).pack(anchor=W)
z.mainloop()