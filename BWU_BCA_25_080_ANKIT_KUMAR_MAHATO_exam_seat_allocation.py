"""
EXAMINATION SEAT ALLOCATION SYSTEM
"""

# --------------------------- INPUT DATA ---------------------------

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


# --------------------------- STUDENT FUNCTIONS ---------------------------

def add_student():
    """Add a student through keyboard input."""
    try:
        roll = int(input("Roll number: "))
        if any(s["roll"] == roll for s in students):
            print("This roll number already exists.")
            return
        name = input("Student name: ").strip()
        section = input("Section: ").strip().upper()
        subject = input("Subject: ").strip()
        preferred = input("Preferred room (R1-R4 or blank): ").strip().upper() or None
        special = input("Special requirement? (y/n): ").strip().lower() == "y"

        if not name or not section or not subject:
            print("Name, section and subject cannot be empty.")
            return
        if preferred is not None and preferred not in rooms:
            print("Invalid room.")
            return

        students.append({
            "roll": roll, "name": name, "section": section,
            "subject": subject, "preferred_room": preferred,
            "special": special
        })
        print("Student added. Generate the seating plan again to include them.")
    except ValueError:
        print("Enter a valid roll number.")


def remove_student():
    try:
        roll = int(input("Enter roll number to remove: "))
        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                for room in seating:
                    seating[room] = {
                        seat: s for seat, s in seating[room].items()
                        if s["roll"] != roll
                    }
                print("Student removed.")
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
        if s["preferred_room"] and s["preferred_room"] not in rooms:
            print("Invalid preferred room for roll", s["roll"])
            return False
    print("Student data is valid.")
    return True


# --------------------------- CAPACITY FUNCTIONS ---------------------------

def calculate_room_capacity():
    return sum(room["capacity"] for room in rooms.values())


def check_capacity():
    total = calculate_room_capacity()
    print(f"Students: {len(students)} | Available seats: {total}")
    if len(students) > total:
        print("Not enough examination seats.")
        return False
    return True


# --------------------------- ALLOCATION FUNCTIONS ---------------------------

def group_students():
    """Return students in a stable, reproducible order."""
    return sorted(students, key=lambda s: (
        not s["special"], not bool(s["preferred_room"]),
        s["preferred_room"] or "", s["roll"]
    ))


def check_seating_constraints(student, room, seat):
    """Check room preference, priority seat and adjacent-seat rules."""
    room_info = rooms[room]
    if student["preferred_room"] and student["preferred_room"] != room:
        return False

    priority = seat in room_info["priority_seats"]
 
    if student["special"] and not priority:
        return False
    if not student["special"] and not priority:
        pass

 
    for neighbour in (seat - 1, seat + 1):
        other = seating[room].get(neighbour)
        if other and (other["section"] == student["section"] or
                      other["subject"] == student["subject"]):
            return False
    return True


def arrange_students():
    """Clear old allocation and create a fresh deterministic arrangement."""
    global seating
    seating = {room: {} for room in rooms}

    if not validate_students() or not check_capacity():
        return False

    ordered = group_students()
    unassigned = ordered[:]

    for room in rooms:
        for seat in range(1, rooms[room]["capacity"] + 1):
            is_priority = seat in rooms[room]["priority_seats"]
            candidates = [
                s for s in unassigned
                if (s["special"] if is_priority else not s["special"])
                and (not s["preferred_room"] or s["preferred_room"] == room)
                and check_seating_constraints(s, room, seat)
            ]
           
            if is_priority and not candidates:
                candidates = [
                    s for s in unassigned
                    if not s["special"]
                    and (not s["preferred_room"] or s["preferred_room"] == room)
                    and check_seating_constraints(s, room, seat)
                ]
            if candidates:
                candidates.sort(key=lambda s: (
                    s["preferred_room"] != room, s["roll"]
                ))
                chosen = candidates[0]
                seating[room][seat] = chosen
                unassigned.remove(chosen)

    if unassigned:
        print("\nCould not allocate every student while satisfying all rules.")
        print("Unallocated roll numbers:", [s["roll"] for s in unassigned])
        print("Try changing room capacities, priority seats or input data.")
        return False

    if validate_arrangement():
        print("\nSeating arrangement generated successfully.")
        return True
    print("Arrangement failed validation.")
    return False


def assign_seats():
    return arrange_students()


def validate_arrangement():
    """Check unique students, unique seats, capacity and all seating rules."""
    allocated = []
    for room, seats in seating.items():
        if len(seats) > rooms[room]["capacity"]:
            return False
        if len(seats) != len(set(seats)):
            return False
        for seat, student in seats.items():
            allocated.append(student["roll"])
            if student["special"] and seat not in rooms[room]["priority_seats"]:
                return False
            if student["preferred_room"] and student["preferred_room"] != room:
                return False
            if not check_seating_constraints(student, room, seat):
                return False

    return len(allocated) == len(students) and len(allocated) == len(set(allocated))


# --------------------------- DISPLAY AND SEARCH ---------------------------

def display_seating_plan():
    if not any(seating.values()):
        print("Generate the seating plan first.")
        return

    for room, seats in seating.items():
        print(f"\nROOM {room} | Invigilator: {rooms[room]['invigilator']}")
        print("-" * 66)
        print(f'{"SEAT":<8} {"ROLL":<8} {"NAME":<12} {"SECTION":<9} SUBJECT')
        for seat in range(1, rooms[room]["capacity"] + 1):
            s = seats.get(seat)
            if s:
                print(f'{seat:<8} {s["roll"]:<8} {s["name"]:<12} '
                      f'{s["section"]:<9} {s["subject"]}')
            else:
                print(f"{seat:<8} {'EMPTY'}")


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
            room, seat, s = result
            print("\nSTUDENT SEAT DETAILS")
            print("Name:", s["name"])
            print("Section:", s["section"])
            print("Subject:", s["subject"])
            print("Examination Room:", room)
            print("Seat Number:", seat)
        else:
            print("Student seat not found. Generate the seating plan first.")
    except ValueError:
        print("Enter a valid roll number.")


# --------------------------- MAIN MENU ---------------------------

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
