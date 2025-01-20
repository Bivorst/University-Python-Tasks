import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

CSV_FILE = "flight_requests.csv"

class Application:
    def __init__(self, destination, flight_number, passenger, date):
        self.destination = destination
        self.flight_number = flight_number
        self.passenger = passenger
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.left = None
        self.right = None

    def __str__(self):
        return f"Flight Number: {self.flight_number}\nDate: {self.date.strftime('%Y-%m-%d')}\nPassenger: {self.passenger}\nDestination: {self.destination}"

    def to_csv_row(self):
        return [self.destination, self.flight_number, self.passenger, self.date.strftime('%Y-%m-%d')]

class FlightApplicationsBST:
    def __init__(self):
        self.root = None

    def insert(self, application):
        if self.root is None:
            self.root = application
        else:
            self._insert(self.root, application)

    def _insert(self, current, application):
        if application.flight_number < current.flight_number:
            if current.left is None:
                current.left = application
            else:
                self._insert(current.left, application)
        else:
            if current.right is None:
                current.right = application
            else:
                self._insert(current.right, application)

    def delete(self, flight_number, date):
        self.root = self._delete(self.root, flight_number, date)

    def _delete(self, root, flight_number, date):
        if root is None:
            return root
        if flight_number < root.flight_number:
            root.left = self._delete(root.left, flight_number, date)
        elif flight_number > root.flight_number:
            root.right = self._delete(root.right, flight_number, date)
        else:
            if root.date == datetime.strptime(date, "%Y-%m-%d"):
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                min_larger_node = self._get_min(root.right)
                root.flight_number = min_larger_node.flight_number
                root.date = min_larger_node.date
                root.passenger = min_larger_node.passenger
                root.destination = min_larger_node.destination
                root.right = self._delete(root.right, root.flight_number, root.date.strftime('%Y-%m-%d'))
        return root

    def _get_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search(self, flight_number, date):
        results = []
        self._search(self.root, flight_number, date, results)
        return results

    def _search(self, node, flight_number, date, results):
        if node is None:
            return
        if flight_number < node.flight_number:
            self._search(node.left, flight_number, date, results)
        elif flight_number > node.flight_number:
            self._search(node.right, flight_number, date, results)
        else:
            if node.date == datetime.strptime(date, "%Y-%m-%d"):
                results.append(node)
            self._search(node.left, flight_number, date, results)
            self._search(node.right, flight_number, date, results)

    def display_all(self):
        applications = []
        self._in_order_traversal(self.root, applications)
        return applications

    def _in_order_traversal(self, node, applications):
        if node is None:
            return
        self._in_order_traversal(node.left, applications)
        applications.append(node)
        self._in_order_traversal(node.right, applications)
        return applications

class FlightApplicationApp:
    def __init__(self, root):
        self.tree = FlightApplicationsBST()
        self.load_from_csv()

        self.root = root
        self.root.title("Flight Request Management")

        self.flight_number_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.destination_var = tk.StringVar()
        self.passenger_var = tk.StringVar()
        self.search_flight_number_var = tk.StringVar()
        self.search_date_var = tk.StringVar()

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        tk.Label(self.frame, text="Flight Number").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.frame, textvariable=self.flight_number_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame, text="Departure Date (YYYY-MM-DD)").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self.frame, textvariable=self.date_var).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame, text="Destination").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(self.frame, textvariable=self.destination_var).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame, text="Passenger Full Name").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(self.frame, textvariable=self.passenger_var).grid(row=3, column=1, padx=5, pady=5)

        tk.Button(self.frame, text="Add Request", command=self.add_application).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(self.frame, text="Display All Requests", command=self.display_all_applications).grid(row=4, column=1, padx=5, pady=5)

        self.search_frame = tk.Frame(root)
        self.search_frame.pack(padx=10, pady=10)

        tk.Label(self.search_frame, text="Search by Flight Number and Date").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.search_frame, textvariable=self.search_flight_number_var).grid(row=0, column=1, padx=5, pady=5)
        tk.Entry(self.search_frame, textvariable=self.search_date_var).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(self.search_frame, text="Search", command=self.search_application).grid(row=0, column=3, padx=5, pady=5)

        self.result_text = tk.Text(root, height=15, width=60)
        self.result_text.pack(padx=10, pady=10)

    def add_application(self):
        flight_number = self.flight_number_var.get().strip()
        date = self.date_var.get().strip()
        destination = self.destination_var.get().strip()
        passenger = self.passenger_var.get().strip()

        if not (flight_number and date and destination and passenger):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            application = Application(destination, flight_number, passenger, date)
            self.tree.insert(application)
            self.save_to_csv(application)
            messagebox.showinfo("Success", "Request added.")
            self.flight_number_var.set('')
            self.date_var.set('')
            self.destination_var.set('')
            self.passenger_var.set('')
        except ValueError:
            messagebox.showerror("Error", "Invalid date.")

    def search_application(self):
        flight_number = self.search_flight_number_var.get().strip()
        date = self.search_date_var.get().strip()

        if not (flight_number and date):
            messagebox.showerror("Error", "Please specify the flight number and date.")
            return

        results = self.tree.search(flight_number, date)

        self.result_text.delete(1.0, tk.END)
        if results:
            for result in results:
                self.result_text.insert(tk.END, str(result) + "\n\n")
        else:
            self.result_text.insert(tk.END, "No requests found.")

    def display_all_applications(self):
        applications = self.tree.display_all()
        self.result_text.delete(1.0, tk.END)
        if applications:
            for app in applications:
                self.result_text.insert(tk.END, str(app) + "\n\n")
        else:
            self.result_text.insert(tk.END, "No requests.")

    def save_to_csv(self, application):
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(application.to_csv_row())

    def load_from_csv(self):
        try:
            with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    destination, flight_number, passenger, date = row
                    self.tree.insert(Application(destination, flight_number, passenger, date))
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightApplicationApp(root)
    root.mainloop()