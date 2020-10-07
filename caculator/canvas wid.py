from tkinter import *

c=Tk()

c.title("canvas design")
cwidth=800
cheight=900

c.geometry(f"{cwidth}x{cheight}")
c1=Canvas(c,width=cwidth,height=cheight)
c1.pack()

c1.create_line(0,0,300,600,fill='blue')

c.mainloop()