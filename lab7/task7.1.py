import pandas as pd
import os
from tkinter import Tk, Label, Entry, Button, Listbox, StringVar, Scrollbar, Frame, Text

csv_file = "employees.csv"

def load_employees(file_name):
    if os.path.exists(file_name):
        return pd.read_csv(file_name)
    else:
        return pd.DataFrame(columns=["Last Name", "Initials", "Position", "Year of Entry", "Salary"])

def save_employees():
    global employees
    employees.to_csv(csv_file, index=False)
    result_text.delete(1.0, "end")
    result_text.insert("end", f"Data saved to file: {csv_file}")

def add_or_edit_employee():
    last_name = last_name_var.get().strip()
    initials = initials_var.get().strip()
    position = position_var.get().strip()
    year = year_var.get().strip()
    salary = salary_var.get().strip()

    if not (last_name and initials and position and year and salary):
        result_text.delete(1.0, "end")
        result_text.insert("end", "Error: Fill in all fields!")
        return

    try:
        year = int(year)
        salary = float(salary)
    except ValueError:
        result_text.delete(1.0, "end")
        result_text.insert("end", "Error: Year and salary must be numeric values!")
        return

    global employees
    employees = employees[employees["Last Name"] != last_name]
    new_row = {"Last Name": last_name, "Initials": initials, "Position": position,
               "Year of Entry": year, "Salary": salary}
    employees = pd.concat([employees, pd.DataFrame([new_row])], ignore_index=True)

    update_listbox()
    result_text.delete(1.0, "end")
    result_text.insert("end", f"Employee {last_name} added/updated.")

def sort_employees_by(criteria):
    global employees
    if criteria == "Last Name":
        employees = employees.sort_values("Last Name")
    elif criteria == "Salary":
        employees = employees.sort_values("Salary", ascending=False)
    elif criteria == "Year of Entry":
        employees = employees.sort_values("Year of Entry")
    update_listbox()

def search_employee():
    last_name = search_var.get().strip()
    row = employees[employees["Last Name"] == last_name]
    result_text.delete(1.0, "end")
    if not row.empty:
        for _, data in row.iterrows():
            result_text.insert("end", f"Last Name: {data['Last Name']}\n")
            result_text.insert("end", f"Initials: {data['Initials']}\n")
            result_text.insert("end", f"Position: {data['Position']}\n")
            result_text.insert("end", f"Year of Entry: {data['Year of Entry']}\n")
            result_text.insert("end", f"Salary: {data['Salary']} rub.\n")
    else:
        result_text.insert("end", f"Employee with last name '{last_name}' not found.")

def update_listbox():
    listbox.delete(0, "end")
    for _, row in employees.iterrows():
        listbox.insert("end", f"{row['Last Name']} - {row['Position']} - {row['Salary']} rub.")

def main():
    global employees, last_name_var, initials_var, position_var, year_var, salary_var, search_var, listbox, result_text

    employees = load_employees(csv_file)

    root = Tk()
    root.title("Employee Management")
    root.geometry("700x500")

    last_name_var = StringVar()
    initials_var = StringVar()
    position_var = StringVar()
    year_var = StringVar()
    salary_var = StringVar()

    Label(root, text="Last Name").grid(row=0, column=0, padx=10, pady=5)
    Entry(root, textvariable=last_name_var).grid(row=0, column=1, padx=10, pady=5)

    Label(root, text="Initials").grid(row=1, column=0, padx=10, pady=5)
    Entry(root, textvariable=initials_var).grid(row=1, column=1, padx=10, pady=5)

    Label(root, text="Position").grid(row=2, column=0, padx=10, pady=5)
    Entry(root, textvariable=position_var).grid(row=2, column=1, padx=10, pady=5)

    Label(root, text="Year of Entry").grid(row=3, column=0, padx=10, pady=5)
    Entry(root, textvariable=year_var).grid(row=3, column=1, padx=10, pady=5)

    Label(root, text="Salary").grid(row=4, column=0, padx=10, pady=5)
    Entry(root, textvariable=salary_var).grid(row=4, column=1, padx=10, pady=5)

    Button(root, text="Add/Edit", command=add_or_edit_employee).grid(row=5, column=0, columnspan=2, pady=10)
    Button(root, text="Save", command=save_employees).grid(row=6, column=0, columnspan=2, pady=10)

    Button(root, text="Sort by Last Name", command=lambda: sort_employees_by("Last Name")).grid(row=7, column=0, columnspan=2, pady=5)
    Button(root, text="Sort by Salary", command=lambda: sort_employees_by("Salary")).grid(row=8, column=0, columnspan=2, pady=5)
    Button(root, text="Sort by Year of Entry", command=lambda: sort_employees_by("Year of Entry")).grid(row=9, column=0, columnspan=2, pady=5)

    Label(root, text="Search by Last Name").grid(row=10, column=0, padx=10, pady=5)
    search_var = StringVar()
    search_entry = Entry(root, textvariable=search_var)
    search_entry.grid(row=10, column=1, padx=10, pady=5)
    Button(root, text="Search", command=search_employee).grid(row=10, column=2, padx=10, pady=5)

    listbox_frame = Frame(root)
    listbox_frame.grid(row=0, column=3, rowspan=9, padx=20, pady=5)

    scrollbar = Scrollbar(listbox_frame)
    scrollbar.pack(side="right", fill="y")

    listbox = Listbox(listbox_frame, width=40, height=20, yscrollcommand=scrollbar.set)
    listbox.pack(side="left", fill="both")

    scrollbar.config(command=listbox.yview)

    result_label = Label(root, text="Search Result:")
    result_label.grid(row=11, column=0, columnspan=3, pady=5)

    result_text = Text(root, height=8, width=60)
    result_text.grid(row=12, column=0, columnspan=3, pady=5)

    update_listbox()

    root.mainloop()

if __name__ == "__main__":
    main()