import tkinter as tk
from tkinter import messagebox
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def validate_phone_number(phone):
    pattern = r'^\d{10}$'
    return re.match(pattern, phone)

def validate_name(name):
    pattern = r'^[^\d]+$'
    return re.match(pattern, name)


def submit_expense():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    category = category_entry.get()

    gender = gender_var.get()
    year = year_spinbox.get()

    if not validate_email(email):
        messagebox.showerror("Error", "Invalid Email")
        return
    if not validate_phone_number(phone):
        messagebox.showerror("Error", "Invalid Phone Number")
        return
    if not validate_name(name):
        messagebox.showerror("Error", "Name cannot contain numeric digits")
        return


    message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nCategory: {category}\nGender: {gender}\nYear: {year}"

    messagebox.showinfo("Expense Details", message)


    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Expense Tracker")

frame = tk.Frame(root, padx=50, pady=60)
frame.pack()


name_label = tk.Label(frame, text="First Name:")
name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

expense_label = tk.Label(frame, text="Last Name:")
expense_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
expense_entry = tk.Entry(frame)
expense_entry.grid(row=1, column=1, padx=5, pady=5)

category_label = tk.Label(frame, text="Passoword:")
category_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
category_entry = tk.Entry(frame)
category_entry.grid(row=2, column=1, padx=5, pady=5)

email_label = tk.Label(frame, text="Email:")
email_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)
email_entry = tk.Entry(frame)
email_entry.grid(row=5, column=1, padx=5, pady=5)

phone_label = tk.Label(frame, text="Phone Number:")
phone_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)
phone_entry = tk.Entry(frame)
phone_entry.grid(row=6, column=1, padx=5, pady=5)


gender_label = tk.Label(frame, text="Gender:")
gender_label.grid(row=7, column=0, sticky="w", padx=5, pady=5)


gender_var = tk.StringVar()
gender_var.set("Select Gender")

gender_options = ["Male", "Female", "Other"]
gender_menu = tk.OptionMenu(frame, gender_var, *gender_options)
gender_menu.grid(row=7, column=1, padx=5, pady=5, sticky="ew")


year_label = tk.Label(frame, text="Year:")
year_label.grid(row=8, column=0, sticky="w", padx=5, pady=5)
year_spinbox = tk.Spinbox(frame, from_=2020, to=2100, width=5)
year_spinbox.grid(row=8, column=1, padx=5, pady=5)

submit_button = tk.Button(frame, text="Submit", command=submit_expense)
submit_button.grid(row=9, columnspan=2, pady=10)

root.mainloop()
