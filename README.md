# Examination Seat Allocation System

A menu-driven Python project that creates examination seating
arrangements using predefined rules and basic Python programming
concepts.

## Project Overview

The Examination Seat Allocation System organises students into
examination rooms and seats. It validates student details and room
capacity, considers preferred rooms, gives priority seats to students
with special requirements, and prevents students from the same section
or subject from sitting in adjacent seats.

The project is implemented in **one Python file: `main.py`**. It does
not use separate `Data` and `Main` folders.

## Features

-   Display all students.
-   Add a student after validating the entered details.
-   Remove a student using their roll number.
-   Generate a seating arrangement automatically.
-   Display the seating plan room by room.
-   Show room-wise occupancy, invigilator and priority-seat details.
-   Search for a student's room and seat using their roll number.
-   Check total available room capacity.
-   Validate student details and the completed seating arrangement.

## Technologies and Python Concepts

-   **Language:** Python 3
-   **External libraries:** None
-   **Concepts:** Lists, dictionaries, tuples, sets, functions, loops,
    conditional statements, sorting, input validation, exception
    handling and formatted strings.
-   **Allocation method:** Iterative backtracking (no recursion).

## Sample Data

The program contains 24 predefined sample students.

  Item                                 Details
  ------------------------------------ ----------------------------------
  Students                             24
  Sections                             A, B, C and D
  Subjects                             Python, DBMS, Networks and Maths
  Rooms                                R1, R2, R3 and R4
  Capacity per room                    6 students
  Total capacity                       24 seats
  Students with preferred rooms        2
  Students with special requirements   2

### Room Details

  Room     Capacity Invigilator   Priority Seats
  ------ ---------- ------------- ----------------
  R1              6 Mr. Sharma    1 and 6
  R2              6 Ms. Roy       1 and 6
  R3              6 Mr. Das       1 and 6
  R4              6 Ms. Sen       1 and 6

## Seating Allocation Rules

1.  Every student must receive exactly one seat.
2.  Room capacity must not be exceeded.
3.  Students from the same section cannot sit in adjacent seats in the
    same room.
4.  Students taking the same subject cannot sit in adjacent seats in the
    same room.
5.  Students with special requirements must receive a priority seat
    (seat 1 or seat 6).
6.  A student's preferred room is tried first when a valid seat is
    available.
7.  The completed arrangement is validated before success is reported.
8.  If a valid arrangement cannot be found, the incomplete arrangement
    is cleared.

**Note:** Adjacent-seat checks apply to consecutive seat numbers within
the same room.

## How to Run

1.  Install Python 3.
2.  Download or clone the project.
3.  Open a terminal in the folder containing `main.py`.
4.  Run:

``` bash
python main.py
```

If required on your system, use:

``` bash
python3 main.py
```

No additional package installation is required.

## Program Menu

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

Enter the corresponding number to select an operation.

## Main Functions

  -----------------------------------------------------------------------
  Function                            Purpose
  ----------------------------------- -----------------------------------
  `add_student()`                     Adds a student after validating the
                                      input.

  `remove_student()`                  Removes a student by roll number.

  `display_students()`                Displays students sorted by roll
                                      number.

  `validate_students()`               Checks duplicate roll numbers and
                                      invalid or incomplete details.

  `calculate_room_capacity()`         Calculates the total capacity of
                                      all rooms.

  `check_capacity()`                  Checks whether enough seats are
                                      available.

  `group_students()`                  Orders special-requirement and
                                      preferred-room students first.

  `check_seating_constraints()`       Checks priority-seat and
                                      adjacent-seat rules.

  `arrange_students()`                Allocates seats using iterative
                                      backtracking.

  `assign_seats()`                    Calls the seating arrangement
                                      function.

  `validate_arrangement()`            Checks that all students are
                                      allocated once and the rules are
                                      followed.

  `display_seating_plan()`            Displays the allocated seats in
                                      each room.

  `generate_room_summary()`           Displays room occupancy,
                                      invigilator and priority-seat
                                      details.

  `find_student_seat()`               Finds a student's room and seat.

  `search_student()`                  Accepts a roll number and displays
                                      the seat details.

  `clear_seating()`                   Clears the previous arrangement
                                      after student data changes.

  `main()`                            Runs the menu and processes user
                                      choices.
  -----------------------------------------------------------------------

## Important Usage Notes

-   Add or remove students before generating the seating plan.
-   Adding or removing a student clears the previous seating
    arrangement.
-   Generate the seating plan before choosing **Display seating plan**
    or **Search student seat**.
-   The sample project has 24 seats. If the number of students exceeds
    total capacity, allocation is stopped.
-   Student and seating details are stored in Python lists and
    dictionaries while the program is running.

## Limitations

-   The project runs in the command line and does not have a graphical
    interface.
-   Changes are not saved permanently after the program closes.
-   Room details, capacities, invigilators and priority seats are
    predefined in the code.
-   The project does not use a database, external API, AI or machine
    learning.

## Future Improvements

-   Save student details and seating plans to a file or database.
-   Allow room and invigilator details to be edited.
-   Generate printable seating reports.
-   Add a graphical user interface.

## Project Information

-   **Project:** Examination Seat Allocation System
-   **Main program file:** `main.py`
-   **Programming language:** Python 3
