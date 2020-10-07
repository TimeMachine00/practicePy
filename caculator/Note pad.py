from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        N.title(os.path.basename(file) + " - Notepad")
        t.delete(1.0, END)
        f = open(file, "r")
        t.insert(1.0, f.read())
        f.close()



def newFile():
    global file
    N.title("Untitled - Notepad")
    file = None
    t.delete(1.0, END)



def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(t.get(1.0, END))
            f.close()

            N.title(os.path.basename(file) + " - Notepad")
            showinfo("Notepad", "your file has been saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(t.get(1.0, END))
        f.close()


def quitApp():
    N.destroy()

def cut():
    t.event_generate(("<<Cut>>"))

def copy():
    t.event_generate(("<<Copy>>"))

def paste():
    t.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by Hussainsha Syed")






if __name__ == '__main__':
    N=Tk()

    N.title("Untitle ----Notepad")
    N.geometry("750x550")
    N.configure(bg="blue")
    N.wm_iconbitmap("ic.ico")


    t=Text(N,font="Times 12")
    file=None
    t.pack(expand=TRUE,fill=BOTH)

    s=Scrollbar(t)
    s.pack(side=RIGHT,fill=Y)
    s.config(command=t.yview)
    t.config(yscrollcommand=s.set)

    z=Menu()
    z1=Menu(z,tearoff=0)

    z1.add_command(label='Open',command=openFile)
    z1.add_command(label='New',command=newFile)
    z1.add_command(label='Save',command=saveFile)
    z1.add_separator()
    z1.add_command(label='Exit',command=quitApp)

    z.add_cascade(label='File',menu=z1)

    z2=Menu(z,tearoff=0)

    z2.add_command(label='Cut',command=cut)
    z2.add_command(label='Copy',command=copy)
    z2.add_command(label='Paste',command=paste)

    z.add_cascade(label='Edit',menu=z2)

    z3=Menu(z,tearoff=0)

    z3.add_command(label='About',command=about)
    z.add_cascade(label='Help',menu=z3)


N.config(menu=z)

N.mainloop()