from tkinter import *
root=Tk()

root.geometry("655x333")
f1=Frame(root,bg="lightblue",borderwidth=8,relief=SUNKEN)
f1.pack(side="left",fill=Y)

f2=Frame(root,borderwidth=8,bg="lightyellow",relief=SUNKEN)
f2.pack(side=TOP,fill=X)

l=Label(f1,text="Project Tkinter - Pycharm",font="timesnewroman")
l.pack(pady=150)
l=Label(f2,text="Welcome to the sublime text",font="timesnewroman",fg="red",)
l.pack() 



root.mainloop()