from tkinter import *
z=Tk()

z.geometry("400x400")
z.resizable(0,0)
z.title('click clock')
'''def show(l):
    z.configure(background='blue')
k=Button(z,text='kiss me', bg='white',fg='blue')
k.bind('<Enter>',lambda e:z.configure(background='red'))
k.bind("<Leave>",show)
k.pack()'''

p=IntVar()
q=IntVar()
r=IntVar()
def show():
    a=p.get()
    b=q.get()
    c=a+b
    r.set(c)
m=Entry(z,textvar=p)
m.pack()
n=Entry(z,textvar=q)
n.pack()
b=Button(z,text='result', command=show)
b.pack()
o=Entry(z,textvar=r)
o.pack()
z.mainloop()