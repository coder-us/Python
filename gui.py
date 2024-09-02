from tkinter import *
# utkarsh_root=Tk()

# # Width x Height
# utkarsh_root.geometry("512x222")
# # Width,height
# utkarsh_root.minsize(400,200)
# # Width,height
# utkarsh_root.maxsize(1000,1000)

# utkarsh=Label(text="Utkarsh is a good boy and this is his GUI")
# utkarsh.pack()
# photo=PhotoImage(file="WhatsApp Image 2024-05-03 at 13.51.12.png")
# utkarsh_lable=Label(image=photo)
# utkarsh_lable.pack()

# Lable and pack attributes 

utkarsh_root=Tk()
utkarsh_root.geometry("500x400")
utkarsh_root.title("My GUI with Utkarsh")

title_label=Label(text="Ready" ,bg="white" ,fg="green" 
                  ,padx=10,pady=10,font=("timesnewroman",28),borderwidth=7,relief=SUNKEN)

title_label.pack(side="bottom",fill=X)



utkarsh_root.mainloop()
