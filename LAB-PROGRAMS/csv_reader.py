from tkinter import filedialog,ttk
import tkinter as tk
import csv

def load_csv_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        # Clear the current treeview
        for row in tree.get_children():
            tree.delete(row)

        # Read and display the CSV file
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            tree["columns"] = header
            for col in header:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            row_num = 1
            for row_data in csv_reader:
                tree.insert("", "end", text=str(row_num), values=row_data)
                row_num += 1

root = tk.Tk()
root.title("CSV Viewer")

load_button = tk.Button(root, text="Browse CSV File", command=load_csv_file)
load_button.pack(pady=10)

tree = ttk.Treeview(root, show="headings")
tree.pack(fill="both", expand=True)

root.mainloop()
