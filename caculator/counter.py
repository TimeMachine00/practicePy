from tkinter import *



z=Tk()

counter = 0
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter+=1
        label.config(text=str(counter))
        label.after(1000,count)
    count()


z.title('Counter')
z.geometry("500x500")

label=Label(z, fg='red')
label.pack()
counter_label(label)

but=Button(text='stop',fg='blue',command=z.destroy())
but.pack()

z.mainloop()
