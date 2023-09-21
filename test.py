from tkinter import*
base = Tk()

base.geometry('500x500')
base.title("Login")

labl_0 = Label(base, text = "Registration Form" ,width=20 , font=("bold", 20))
labl_0.place(x=90,y=50)

labl_1 = Label(base, text="Username ", width= 20, font=("bold",10))
labl_1.place(x=80, y=130)

entry_1 =Entry(base)
entry_1.place(x=240, y= 130)

labl_2 = Label(base, text= "Password", width=20, font=("bold",10))
labl_2.place(x=68, y=180)

entry_2 = Entry(base)
entry_2.place(x=240, y=180)

Button(base, text='Submit', width= 20, bg="Brown", fg="white").place(x=180, y=380)

base.mainloop()
print("registration form is created successful")