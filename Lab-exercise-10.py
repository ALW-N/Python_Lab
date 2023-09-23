from logging import root
from tkinter import*
import re
from tkinter import ttk
import tkinter


def validate_Name(first_name):
    if first_name.isalpha():
        return True
    else:
        return False


def on_submit():
    first_name = entry_0.get()
    if validate_Name(first_name):
        print(f"first Name: {first_name}")
    else:
        print("Invalid Name")

base = Tk()
base.geometry("580x500")
base.title("Form")

labl_0 = Label(base, text="First Name:", width=20, font=("bold", 10))
labl_0.place(x=5, y=50)

labl_1 = Label(base, text="Last Name:", width=20, font=("bold", 10))
labl_1.place(x=250, y=50)

labl_2 = Label(base, text="Email:", width=20, font=("bold", 10))
labl_2.place(x=1, y=100)

labl_3 = Label(base, text="Gender:", width=20, font=("bold", 10))
labl_3.place(x=1, y=150)

labl_4 = Label(base, text="Phone number:", width=20, font=("bold", 10))
labl_4.place(x=1, y=200)

labl_5 = Label(base, text="Password:", width=20, font=("bold", 10))
labl_5.place(x=1, y=250)

entry_0 = Entry(base, validate="key", validatecommand=(
    base.register(validate_Name), "%S"))
entry_0.place(x=130, y=50)

entry_1 = Entry(base, validate="key", validatecommand=(
    base.register(validate_Name), "%S"))
entry_1.place(x=390, y=50)

entry_2 = Entry(base)
entry_2.place(x=130, y=100)

entry_3 = Entry(base)
entry_3.place(x=130, y=200)

entry_4 = Entry(base)
entry_4.place(x=130, y=250)


ttk.Label(base, text="Gender:",
          font=("Times New Roman", 10))

# Combobox creation
n = tkinter.StringVar()
gender = ttk.Combobox(base, width=27, textvariable=n)

# Adding combobox drop down list
gender['values'] = (' Male',
                    ' Female',
                    ' Others'
                    )

gender.place(x=130, y=150)
gender.current()

Button(base, text='Sign Up', width=20, bg="Brown",
       fg="white", command=on_submit).place(x=180, y=380)

base.mainloop()
