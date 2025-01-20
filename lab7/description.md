# Laboratory Work 7

## Overview
Laboratory work 7 consists of two tasks focusing on managing data through different structures and interfaces. Each task involves creating a program with specific functionality to manipulate and display data. Below is a detailed description of each task and the program functionality.

---

## Task 7.1: Employee Management
### Objective:
Manage a list of employees with details such as last name, initials, job title, year of employment, and salary.

### Features:
1. **Add or Edit Employee:**
   - Add new employees to the list or edit existing ones by providing the last name and other details.
2. **Sort Employees:**
   - Sort by last name, salary, or year of employment.
3. **Search Employee:**
   - Retrieve details of an employee by entering their last name.
4. **Save to File:**
   - Save the list of employees to a CSV file with the same or a new name.
5. **User Interface:**
   - Implemented using `Tkinter` with fields for employee details and buttons for actions.

### Technologies Used:
- `pandas` for data handling.
- `Tkinter` for GUI development.
- CSV file format for data storage.

### Program Flow:
1. Load employee data from a CSV file.
2. Interact with the GUI to add, edit, sort, search, and save employees.
3. Update the displayed list in the GUI dynamically.

---

## Task 7.2: Flight Ticket Applications
### Objective:
Manage applications for flight tickets using a binary search tree (BST).

### Features:
1. **Add Application:**
   - Include a destination, flight number, passenger details, and desired flight date.
2. **Remove Applications:**
   - Remove applications based on flight number and date.
3. **Search Applications:**
   - Find and display applications matching a specific flight number and date.
4. **Display All Applications:**
   - Show all stored applications in the BST.
5. **Persist Data:**
   - Save applications to a CSV file and load them upon program start.

### Technologies Used:
- Binary Search Tree (BST) for data organization.
- `Tkinter` for GUI development.
- CSV file format for data storage.

### Program Flow:
1. Load applications from a CSV file into a BST.
2. Interact with the GUI to add, delete, search, and display applications.
3. Save updated data back to the CSV file.

---

## How to Run the Programs

### Prerequisites:
1. Python 3.8 or later.
2. Install required libraries:
   ```bash
   pip install pandas
   ```

### Execution:
1. Save the provided code for each task into separate Python files (`task7_1.py` and `task7_2.py`).
2. Run each script using Python:
   ```bash
   python task7_1.py
   python task7_2.py
   ```

---

## Notes
- Ensure CSV files (`employees.csv` and `flight_requests.csv`) are present in the same directory as the scripts.
- GUI fields must be filled accurately for smooth operation.
- Application dates must follow the `YYYY-MM-DD` format.

---

## Author
Developed as part of the **Laboratory Work 7** for managing structured data with Python.