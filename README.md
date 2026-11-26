# Examination Seat Allocation System

A Python-based, rule-driven application that automatically prepares
examination seating arrangements for university students. The system
allocates students to available rooms while checking room capacity,
section separation, subject separation, preferred-room requests, and
priority seats for students with special requirements.

## Project Overview

Universities may need to arrange many students across several
examination rooms. Preparing these arrangements manually can take time
and may lead to duplicate seat assignments or violations of seating
rules.

This project provides a menu-driven Python application that stores
student and room details separately, generates a reproducible seating
plan, validates the final allocation, displays room-wise arrangements,
and allows a student's seat to be found using their roll number.

## Features

-   **Student management:** Display, add, and remove student records.
-   **Automatic seat allocation:** Assign students to available seats
    using predefined rules.
-   **Section separation:** Students from the same section cannot occupy
    adjacent seats in the same room.
-   **Subject separation:** Students appearing for the same subject
    cannot occupy adjacent seats in the same room.
-   **Room capacity checking:** Prevents a room from exceeding its
    seating capacity.
-   **Unique allocation:** Each student is assigned exactly one seat,
    and each seat is assigned to at most one student.
-   **Preferred room:** Attempts to place a student in their preferred
    room when a valid seat is available.
-   **Priority seating:** Students marked with special requirements are
    assigned priority seats.
-   **Invigilator details:** Displays the assigned invigilator with each
    room's seating plan.
-   **Student seat lookup:** Searches by roll number and displays the
    student's room and seat number.
-   **Room-wise summary:** Shows occupied seats, room capacity,
    invigilator, and priority seat information.
-   **Reproducible results:** Uses a fixed ordering and no random
    allocation.

## Technology Used

  Item                      Details
  ------------------------- --------------------------
  Programming language      Python 3
  Application type          Command-line application
  Data structures           Lists and dictionaries
  Development environment   VS Code / Python IDLE
  External libraries        None
  Database                  Not used

## Project Structure

``` text
Exam_Seat_Allocation_Project/
│
├── Data/
│   ├── __init__.py
│   └── data.py
│
├── Main/
│   ├── __init__.py
│   └── main.py
│
└── README.md
```

### Folder Description

-   **Data/data.py** --- Contains the sample student records and
    examination room details.
-   **Main/main.py** --- Contains the menu, validation, seat allocation,
    display, summary, and search functions.
-   **README.md** --- Provides project information and instructions.

Keep the `Data` and `Main` folders inside the same project directory.
The folder names are case-sensitive on some operating systems.

## Sample Dataset

The project includes the following minimum test dataset:

  Dataset item                           Included
  ------------------------------------ ----------
  Students                                     24
  Sections                                      4
  Examination subjects                          4
  Examination rooms                             4
  Capacity per room                             6
  Total room capacity                          24
  Students with preferred rooms                 2
  Students with special requirements            2

### Sample Examination Rooms

  Room     Capacity Invigilator   Priority seats
  ------ ---------- ------------- ----------------
  R1              6 Mr. Sharma    1, 6
  R2              6 Ms. Roy       1, 6
  R3              6 Mr. Das       1, 6
  R4              6 Ms. Sen       1, 6

Student records contain a roll number, name, section, examination
subject, preferred room (if any), and special-requirement status.

## Seating Rules

The application checks the following rules while creating the seating
plan:

1.  **Section separation:** Adjacent seats must not be occupied by
    students from the same section.
2.  **Subject separation:** Adjacent seats must not be occupied by
    students appearing for the same subject.
3.  **Room capacity:** The number of students in a room must not exceed
    its capacity.
4.  **Unique student allocation:** Every student must receive exactly
    one seat.
5.  **Unique seat allocation:** A seat cannot be assigned to more than
    one student.
6.  **Preferred room:** The system tries to use the student's preferred
    room when a valid seat is available.
7.  **Special requirement:** Students marked with special requirements
    must be assigned priority seats.
8.  **Invigilator information:** Each room's seating plan displays its
    assigned invigilator.
9.  **Reproducibility:** The same input data and rules produce the same
    allocation order; random allocation is not used.

Adjacent seats are treated as consecutive seat numbers within the same
room.

## How to Run the Project

### 1. Install Python

Install Python 3 if it is not already installed. Check the installation
with:

``` bash
python --version
```

On some systems, use:

``` bash
python3 --version
```

### 2. Download or Clone the Repository

Clone the repository:

``` bash
git clone <your-repository-url>
```

Or download the repository as a ZIP file and extract it.

### 3. Open the Project Folder

Open the extracted `Exam_Seat_Allocation_Project` folder in VS Code or a
terminal.

### 4. Run the Application

From the project root directory, run:

``` bash
python Main/main.py
```

If your system uses `python3`, run:

``` bash
python3 Main/main.py
```

No third-party package installation is required.

## Application Menu

When the application starts, it displays the following menu:

``` text
===== EXAMINATION SEAT ALLOCATION SYSTEM =====
1. Display students
2. Add student
3. Remove student
4. Generate seating arrangement
5. Display seating plan
6. Room-wise summary
7. Search student seat
8. Check total capacity
9. Exit
```

Choose an option by entering its number.

**Recommended first run:** Select option `4` to generate the seating
arrangement. Then select option `5` to view the room-wise seating plan,
option `6` to view the room summary, or option `7` to search for a
student.

## Main Python Functions

  -----------------------------------------------------------------------
  Function                            Purpose
  ----------------------------------- -----------------------------------
  `add_student()`                     Adds a student record after
                                      checking the entered details.

  `remove_student()`                  Removes a student using their roll
                                      number.

  `display_students()`                Displays all student records.

  `validate_students()`               Checks student data and duplicate
                                      roll numbers.

  `calculate_room_capacity()`         Calculates the total capacity of
                                      all rooms.

  `check_capacity()`                  Checks whether enough seats are
                                      available.

  `group_students()`                  Sorts students in a fixed,
                                      reproducible order.

  `check_seating_constraints()`       Checks priority-seat and
                                      adjacent-seat conditions.

  `arrange_students()`                Generates the seating arrangement.

  `assign_seats()`                    Calls the seat allocation
                                      operation.

  `validate_arrangement()`            Checks the completed seating plan.

  `display_seating_plan()`            Displays the seating arrangement
                                      room by room.

  `generate_room_summary()`           Displays room capacity and
                                      invigilator information.

  `find_student_seat()`               Finds a student's room and seat
                                      using the roll number.

  `search_student()`                  Takes a roll number and displays
                                      the student's seat details.
  -----------------------------------------------------------------------

## Python Concepts Demonstrated

-   Variables and data types
-   Lists and dictionaries
-   Conditional statements (`if`, `elif`, `else`)
-   `for` and `while` loops
-   User-defined functions
-   Function arguments and return values
-   String methods
-   Sorting with `sorted()` and `lambda`
-   Searching and data validation
-   Deterministic allocation using iterative backtracking

The allocation process uses **iterative backtracking**, not recursion,
to try alternative seat assignments when a previous choice prevents a
complete valid arrangement.

## Limitations

-   The application uses a command-line interface; it does not include a
    graphical user interface.
-   Student and room data are maintained in Python files and memory; no
    database is used.
-   Student changes made while the application is running are not
    automatically saved back to `data.py`.
-   The preferred room is used when a valid seat is available; if the
    constraints prevent a complete valid allocation, the program reports
    that it could not find an arrangement.
-   The sample student and room records are demonstration data and
    should be replaced with actual examination records before real use.

## Future Improvements

Possible future enhancements include:

-   Saving student records and seating plans to CSV files.
-   Generating printable PDF or Excel seating plans.
-   Adding a graphical user interface.
-   Supporting configurable room layouts and seat positions.
-   Allowing administrators to edit room capacities, invigilators, and
    priority seats through the application.

## Project Information

**Project Title:** Examination Seat Allocation System Using Rule-Based
Student Allocation\
**Programming Language:** Python\
**Project Type:** Academic Project\
**Student:** Ankit Kumar Mahato\
**Student Code:** BWU/BCA/25/080\
**Department:** Computational Sciences\
**Institution:** Brainware University

## References

-   [Python Official Documentation](https://docs.python.org/3/)
-   [Python Tutorial](https://docs.python.org/3/tutorial.html)
