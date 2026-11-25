"""EXAMINATION SEAT ALLOCATION SYSTEM

"""

students = [
    {"roll": 1001, "name": "Aarav",  "section": "A", "subject": "Python",  "preferred_room": None, "special": False},
    {"roll": 1002, "name": "Diya",   "section": "B", "subject": "DBMS",    "preferred_room": None, "special": False},
    {"roll": 1003, "name": "Ishaan", "section": "C", "subject": "Networks","preferred_room": None, "special": False},
    {"roll": 1004, "name": "Meera",  "section": "D", "subject": "Maths",   "preferred_room": None, "special": False},
    {"roll": 1005, "name": "Rohan",  "section": "A", "subject": "DBMS",    "preferred_room": "R2", "special": False},
    {"roll": 1006, "name": "Anaya",  "section": "B", "subject": "Networks","preferred_room": None, "special": False},
    {"roll": 1007, "name": "Kabir",  "section": "C", "subject": "Maths",   "preferred_room": None, "special": False},
    {"roll": 1008, "name": "Sara",   "section": "D", "subject": "Python",  "preferred_room": None, "special": False},
    {"roll": 1009, "name": "Arjun",  "section": "A", "subject": "Networks","preferred_room": None, "special": False},
    {"roll": 1010, "name": "Myra",   "section": "B", "subject": "Maths",   "preferred_room": None, "special": False},
    {"roll": 1011, "name": "Vivaan", "section": "C", "subject": "Python",  "preferred_room": None, "special": False},
    {"roll": 1012, "name": "Aisha",  "section": "D", "subject": "DBMS",    "preferred_room": "R3", "special": False},
    {"roll": 1013, "name": "Advik",  "section": "A", "subject": "Maths",   "preferred_room": None, "special": False},
    {"roll": 1014, "name": "Ira",    "section": "B", "subject": "Python",  "preferred_room": None, "special": False},
    {"roll": 1015, "name": "Reyansh","section": "C", "subject": "DBMS",    "preferred_room": None, "special": False},
    {"roll": 1016, "name": "Kiara",  "section": "D", "subject": "Networks","preferred_room": None, "special": False},
    {"roll": 1017, "name": "Atharv", "section": "A", "subject": "Python",  "preferred_room": None, "special": True},
    {"roll": 1018, "name": "Navya",  "section": "B", "subject": "DBMS",    "preferred_room": None, "special": True},
    {"roll": 1019, "name": "Krish",  "section": "C", "subject": "Networks","preferred_room": None, "special": False},
    {"roll": 1020, "name": "Tara",   "section": "D", "subject": "Maths",   "preferred_room": None, "special": False},
    {"roll": 1021, "name": "Dhruv",  "section": "A", "subject": "DBMS",    "preferred_room": None, "special": False},
    {"roll": 1022, "name": "Saanvi", "section": "B", "subject": "Networks","preferred_room": None, "special": False},
    {"roll": 1023, "name": "Yash",   "section": "C", "subject": "Maths",   "preferred_room": None, "special": False},
    {"roll": 1024, "name": "Riya",   "section": "D", "subject": "Python",  "preferred_room": None, "special": False},
]

rooms = {
    "R1": {"capacity": 6, "invigilator": "Mr. Sharma", "priority_seats": [1, 6]},
    "R2": {"capacity": 6, "invigilator": "Ms. Roy", "priority_seats": [1, 6]},
    "R3": {"capacity": 6, "invigilator": "Mr. Das", "priority_seats": [1, 6]},
    "R4": {"capacity": 6, "invigilator": "Ms. Sen", "priority_seats": [1, 6]},
}


seating = {room: {} for room in rooms}


def add_student():
    """Add a new student after validating the entered details."""
    try:
        roll = int(input("Roll number: "))
        if any(s["roll"] == roll for s in students):
            print("This roll number already exists.")
            return
        name = input("Student name: ").strip()
        section = input("Section: ").strip().upper()
        subject = input("Examination subject: ").strip()
        preferred = input("Preferred room (R1-R4 or blank): ").strip().upper() or None
        special = input("Special requirement? (y/n): ").strip().lower()

        if not name or not section or not subject:
            print("Name, section and subject cannot be empty.")
            return
        if preferred is not None and preferred not in rooms:
            print("Invalid room. Choose R1, R2, R3 or R4.")
            return
        if special not in ("y", "n"):
            print("Enter y or n for special requirement.")
            return

        students.append({
            "roll": roll, "name": name, "section": section,
            "subject": subject, "preferred_room": preferred,
            "special": special == "y"
        })
        clear_seating()
        print("Student added. Generate the seating plan again.")
    except ValueError:
        print("Roll number must be an integer.")


def clear_seating():
    """Clear the old arrangement after student data changes."""
    global seating
    seating = {room: {} for room in rooms}


def remove_student():
    try:
        roll = int(input("Enter roll number to remove: "))
        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                clear_seating()
                print("Student removed. Generate the seating plan again.")
                return
        print("Student not found.")
    except ValueError:
        print("Enter a valid roll number.")


def display_students():
    print("\nROLL  NAME       SECTION  SUBJECT    PREFERRED  SPECIAL")
    print("-" * 62)
    for s in sorted(students, key=lambda x: x["roll"]):
        print(f'{s["roll"]:<5} {s["name"]:<10} {s["section"]:<8} '
              f'{s["subject"]:<10} {str(s["preferred_room"] or "-"):<10} '
              f'{"Yes" if s["special"] else "No"}')


def validate_students():
    rolls = [s["roll"] for s in students]
    if len(rolls) != len(set(rolls)):
        print("Invalid data: duplicate roll numbers.")
        return False
    for s in students:
        if not s["name"].strip() or not s["section"].strip() or not s["subject"].strip():
            print("Invalid student details for roll:", s["roll"])
            return False
        if s["preferred_room"] and s["preferred_room"] not in rooms:
            print("Invalid preferred room for roll:", s["roll"])
            return False
    return True


def calculate_room_capacity():
    return sum(info["capacity"] for info in rooms.values())


def check_capacity():
    total = calculate_room_capacity()
    print(f"Students: {len(students)} | Available seats: {total}")
    if len(students) > total:
        print("Not enough examination seats.")
        return False
    return True


def group_students():
    """Sort students deterministically; special and preferred students first."""
    return sorted(students, key=lambda s: (
        not s["special"], s["preferred_room"] is None,
        s["preferred_room"] or "", s["roll"]
    ))


def check_seating_constraints(student, room, seat, current_seating=None):
    """Check priority-seat and adjacent-seat rules for one proposed seat."""
    if current_seating is None:
        current_seating = seating
    if student["special"] and seat not in rooms[room]["priority_seats"]:
        return False

    for neighbour in (seat - 1, seat + 1):
        other = current_seating[room].get(neighbour)
        if other and (other["section"] == student["section"] or
                      other["subject"] == student["subject"]):
            return False
    return True


def arrange_students():
    """Allocate all students using deterministic, iterative backtracking."""
    global seating
    seating = {room: {} for room in rooms}

    if not validate_students() or not check_capacity():
        return False

    ordered = group_students()
    if not ordered:
        print("There are no students to allocate.")
        return True

    # Build a fixed list of all available seats.
    all_seats = []
    for room, info in rooms.items():
        for seat in range(1, info["capacity"] + 1):
            all_seats.append((room, seat))

    # Candidate seats are ordered to honour preferences and priority seats first.
    options = []
    for student in ordered:
        possible = []
        for room, seat in all_seats:
            if student["special"] and seat not in rooms[room]["priority_seats"]:
                continue
            possible.append((room, seat))
        possible.sort(key=lambda item: (
            student["preferred_room"] is not None and item[0] != student["preferred_room"],
            item[0], item[1]
        ))
        options.append(possible)

    # Iterative backtracking avoids recursion and tries alternatives if a choice blocks later students.
    next_choice = [0] * len(ordered)
    assigned = [None] * len(ordered)
    index = 0

    while index >= 0 and index < len(ordered):
        student = ordered[index]
        placed = False

        while next_choice[index] < len(options[index]):
            room, seat = options[index][next_choice[index]]
            next_choice[index] += 1

            if seat in seating[room]:
                continue
            if not check_seating_constraints(student, room, seat):
                continue

            # If a preferred room has any currently valid seat, try it before other rooms.
            if student["preferred_room"] and room != student["preferred_room"]:
                preferred_valid = False
                for pref_seat in range(1, rooms[student["preferred_room"]]["capacity"] + 1):
                    if pref_seat not in seating[student["preferred_room"]] and check_seating_constraints(
                        student, student["preferred_room"], pref_seat
                    ):
                        preferred_valid = True
                        break
                if preferred_valid:
                    continue

            seating[room][seat] = student
            assigned[index] = (room, seat)
            index += 1
            if index < len(ordered):
                next_choice[index] = 0
            placed = True
            break

        if not placed:
            next_choice[index] = 0
            if index == 0:
                break
            index -= 1
            previous = assigned[index]
            if previous is not None:
                old_room, old_seat = previous
                del seating[old_room][old_seat]
                assigned[index] = None

    if index == len(ordered) and validate_arrangement():
        print("\nSeating arrangement generated successfully.")
        return True

    clear_seating()
    print("Could not find a valid arrangement for all students.")
    print("Check room capacities, priority seats and student constraints.")
    return False


def assign_seats():
    return arrange_students()


def validate_arrangement():
    """Validate capacity, unique allocation, preference and adjacency rules."""
    allocated_rolls = []
    for room, seats in seating.items():
        if len(seats) > rooms[room]["capacity"]:
            return False
        for seat, student in seats.items():
            if seat < 1 or seat > rooms[room]["capacity"]:
                return False
            allocated_rolls.append(student["roll"])
            if student["special"] and seat not in rooms[room]["priority_seats"]:
                return False
            if not check_seating_constraints(student, room, seat):
                return False
            for neighbour in (seat - 1, seat + 1):
                other = seats.get(neighbour)
                if other and (other["section"] == student["section"] or
                              other["subject"] == student["subject"]):
                    return False

    # Every student must appear exactly once.
    expected = [s["roll"] for s in students]
    return (len(allocated_rolls) == len(expected) and
            len(allocated_rolls) == len(set(allocated_rolls)) and
            set(allocated_rolls) == set(expected))


def display_seating_plan():
    if not any(seating.values()):
        print("Generate the seating plan first.")
        return
    for room, seats in seating.items():
        print(f"\nROOM {room} | Invigilator: {rooms[room]['invigilator']}")
        print("-" * 66)
        print(f'{"SEAT":<8} {"ROLL":<8} {"NAME":<12} {"SECTION":<9} SUBJECT')
        for seat in range(1, rooms[room]["capacity"] + 1):
            student = seats.get(seat)
            if student:
                print(f'{seat:<8} {student["roll"]:<8} {student["name"]:<12} '
                      f'{student["section"]:<9} {student["subject"]}')
            else:
                print(f"{seat:<8} EMPTY")


def generate_room_summary():
    print("\nROOM-WISE SUMMARY")
    print("-" * 55)
    for room, info in rooms.items():
        count = len(seating[room])
        print(f'{room}: {count}/{info["capacity"]} seats | '
              f'Invigilator: {info["invigilator"]} | '
              f'Priority seats: {info["priority_seats"]}')


def find_student_seat(roll):
    for room, seats in seating.items():
        for seat, student in seats.items():
            if student["roll"] == roll:
                return room, seat, student
    return None


def search_student():
    try:
        roll = int(input("Enter student roll number: "))
        result = find_student_seat(roll)
        if result:
            room, seat, student = result
            print("\nSTUDENT SEAT DETAILS")
            print("Name:", student["name"])
            print("Section:", student["section"])
            print("Subject:", student["subject"])
            print("Examination Room:", room)
            print("Seat Number:", seat)
        else:
            print("Student seat not found. Generate the seating plan first.")
    except ValueError:
        print("Enter a valid roll number.")


def main():
    while True:
        print("\n===== EXAMINATION SEAT ALLOCATION SYSTEM =====")
        print("1. Display students")
        print("2. Add student")
        print("3. Remove student")
        print("4. Generate seating arrangement")
        print("5. Display seating plan")
        print("6. Room-wise summary")
        print("7. Search student seat")
        print("8. Check total capacity")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            display_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            arrange_students()
        elif choice == "5":
            display_seating_plan()
        elif choice == "6":
            generate_room_summary()
        elif choice == "7":
            search_student()
        elif choice == "8":
            check_capacity()
        elif choice == "9":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
