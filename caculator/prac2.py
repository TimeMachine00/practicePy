from  tkinter import  *
A=Tk()

A.geometry("400x400")
A.resizable(0,0)

x=IntVar()

y=IntVar()

z=IntVar()
def show():
    a = x.get()
    b = y.get()
    c = (a + b)
    z.set(c)
e1=Entry(A,fg='Blue',textvar=x)
e1.pack()
e2=Entry(A,fg='Blue',textvar=y)
e2.pack()
b=Button(A,text='result',command=show)
b.pack()
e3=Entry(A,fg='Blue',textvar=z)
e3.pack()

A.mainloop()