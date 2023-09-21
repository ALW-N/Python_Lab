from tkinter import*

base = Tk()
base.geometry("580x500")
base.title("Form")

labl_0 = Label(base, text="First Name:", width= 20, font=("bold",10))
labl_0.place(x=5, y=50)

labl_1 = Label(base, text="Last Name:", width= 20, font=("bold",10))
labl_1.place(x=250,y=50)

labl_2 = Label(base, text="Email:", width=20, font=("bold",10))
labl_2.place(x=1,y=100)

labl_3 = Label(base, text="Gender:", width= 20, font = ("bold",10))
labl_3.place(x=1,y=150)

labl_4 = Label(base, text="Phone number:", width= 20, font = ("bold",10))
labl_4.place(x=1,y=200)

labl_5 = Label(base, text="Password:", width= 20, font = ("bold",10))
labl_5.place(x=1,y=250)

entry_0 = Entry(base)
entry_0.place(x=130, y=50)

entry_1 = Entry(base)
entry_1.place(x=390,y=50)

entry_2 = Entry(base)
entry_2.place(x=130,y=100)

entry_3 = Entry(base)
entry_3.place(x=130,y=200)

entry_4 = Entry(base)
entry_4.place(x=130,y=250)

varblbl = IntVar()
Radiobutton(base, text="Male",padx = 5, variable=varblbl, value=1).place(x=130,y=150)
Radiobutton(base, text="Female",padx = 20, variable=varblbl, value=2).place(x=200,y=150)
Radiobutton(base, text="Other",padx = 20, variable=varblbl, value=2).place(x=300,y=150)

Button(base, text='Sign Up', width= 20, bg="Brown", fg="white").place(x=180, y=380)

base.mainloop()
