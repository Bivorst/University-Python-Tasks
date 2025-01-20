# University Python Programming Lab Works

This project includes all the Python programming lab works completed during university, as well as the course project. Each work involved various tasks related to mathematical modeling, data processing, and graphical representation.

## Table of Contents

1. [Lab Work 1: Formula Calculations](#Lab-Work-1)
2. [Lab Work 2: Function Value Calculation and Region Check](#Lab-Work-2)
3. [Lab Work 3: Tabular Calculations and Integral Sine](#Lab-Work-3)
4. [Lab Work 4: Operations with 1D Arrays](#Lab-Work-4)
5. [Lab Work 5: Working with Square Matrices](#Lab-Work-5)
6. [Lab Work 6: File Input/Output](#Lab-Work-6)
7. [Lab Work 7: Working with Text and Binary Data](#Lab-Work-7)
8. [Lab Work 8: Graphical Representation of Data](#Lab-Work-8)
9. [Course Project](#Course-Project)

## Lab Work 1
### Task 1:
Write a program to calculate the formulas. Example:  
- z1 = (2 * cos(a) * sin(2a) - sin(a)) / (cos(a) - 2 * sin(a) * sin(2a))
- z2 = tan(3a)
Prepare test examples using a calculator or Excel spreadsheet.

## Lab Work 2
### Task 1:
Write a program that calculates the value of a function based on the entered argument value, given in graphical form.

### Task 2:
Write a program to determine if a point with given coordinates lies inside a shaded region. The result will be either "Inside" or "Outside."

## Lab Work 3
### Task 1:
Calculate and display the values of a function on the interval from Xstart to Xend with a step of dx, including a header and a table header.

### Task 2:
For 10 shots, whose coordinates are generated randomly, output text messages about whether the shot hits the target (based on Task 2 of Lab Work 2).

### Task 3:
Calculate and display the values of the integral sine function, defined by a power series, on the interval from Xstart to Xend with a step of dx and an accuracy of ε. The table should contain the argument value, function value, and the number of summed series terms.

## Lab Work 4
### Task 1:
In a 1D array consisting of n integer elements, calculate:
1. The sum of elements with odd indices.
2. The sum of elements located between the first and last negative elements.
3. Compress the array by removing elements whose absolute value is less than or equal to 1, and fill the freed-up space at the end with zeros.

## Lab Work 5
### Task 1:
Given an integer square matrix, calculate:
1. The product of elements in rows that do not contain negative elements.
2. The minimum of the sums of elements of diagonals parallel to the secondary diagonal.

## Lab Work 6
### Task 1:
Modify the programs from Lab Works 1, 4, and 5 to read input data from files and write the results to a file instead of using keyboard input and screen output.

### Task 2:
For Lab Work 5, we will create an array using `random()`, store it in a text file, and read it back. We'll also calculate the mean and variance of the array using NumPy functions.

## Lab Work 7
### Task 1:
A text file contains a list of employees, including their surname, position, date of employment, and salary. Write a program that:
- Allows corrections or additions to the list from the keyboard.
- Sorts the list by surname, salary, or year of employment.
- Displays information about an employee by surname.
- Writes the list to a file (under the same or a new name).

### Task 2:
Create a program that stores current flight ticket applications. Each application contains:
- Destination
- Flight number
- Passenger's surname and initials
- Desired departure date
The program should support:
- Storing applications in a binary tree.
- Adding and deleting applications.
- Displaying applications based on the flight number and date, then deleting them.
- Displaying all applications.

## Lab Work 8
### Task 1:
Using the code from Lab Work 2, Task 1, and Lab Work 2, Task 2, and one of the graphical modules of Python, write programs that graphically illustrate the function and region:
- **Task 1**: Solve the inverse problem — plot the function using the code written for this task.
- **Task 2**: Create a graphical image by generating points with random coordinates (up to 10,000 points). Estimate the area of the shaded region using the Monte Carlo method and compare it with the actual area.
- **Task 3**: Display the graphs of two functions on the interval from Xstart to Xend with step dx. One function is defined by the Taylor series, and the other is defined by user input for parameter b.

## Course Project: Database of Musical Instruments in Songs
### 1. Introduction
#### 1.1 Website Name
- **Website Name**: "Instruments in Music"

#### 1.2 Purpose and Scope
The website is designed to store and display a database of musical instruments mentioned in various musical works. Users will be able to search for, view, and add information about instruments, as well as receive recommendations based on their preferences.

### 2. Program Requirements
#### 2.1 Functional Requirements
The website must support the following functions:
- Search instruments by name, type, or song.
- View detailed information about each instrument.

#### 2.2 Reliability Requirements

##### 2.2.1 Reliable Operation
The reliable operation of the website must be ensured by the following:
- Use of licensed software.
- Regular database backups.

##### 2.2.2 Recovery Time
The recovery time after a failure, caused by hardware issues or database problems, must not exceed 30 minutes, provided the technical and software environment is maintained properly.

#### 2.3 Interface Requirements
The graphical interface should include the following structure:
- User-friendly navigation.
- Search functionality with filters.
- A responsive design for mobile and desktop usage.
- Clear layout for displaying instrument details and recommendations.# University-Python-Tasks

