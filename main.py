# ATTENDANCE MONITORING SYSTEM
from datetime import datetime
import re


# Data Storage
students = {}               # {student_id: name}
attendance_records = {}     # {student_id: [(date, status), ...]}


def is_valid_student_id(sid):
    """Allow format like: 02-2627-123456 — numbers and hyphens only"""
    if not sid:
        return False
    return bool(re.fullmatch(r'[0-9-]+', sid))


def is_valid_name(name):
    """Name: letters and spaces only"""
    return bool(re.fullmatch(r'[A-Za-z\s]+', name.strip()))


# ========== TEACHER FUNCTIONS ==========
def add_student():
    print("\n--- Add Student ---")
    while True:
        sid = input("Enter Student ID (e.g., 02-2627-123456): ").strip()
        if not is_valid_student_id(sid):
            print("[ERROR] Invalid! Use numbers and hyphens only — no letters.")
            continue
        if sid in students:
            print("[ERROR] Student ID already exists!")
            continue
        break
   
    while True:
        name = input("Enter Student Name: ").strip()
        if not name:
            print("[ERROR] Name cannot be empty!")
            continue
        if not is_valid_name(name):
            print("[ERROR] Invalid! Use letters only.")
            continue
        break
   
    students[sid] = name
    attendance_records[sid] = []
    print(f"[SUCCESS] Student added: {name}")


def mark_attendance():
    print("\n--- Mark Students Attendance ---")
    if not students:
        print("[INFO] No students found. Add students first.")
        return
   
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_input:
        date_input = datetime.now().strftime("%Y-%m-%d")
   
    print(f"\nDate: {date_input}")
    print("-" * 45)
   
    for sid, name in students.items():
        while True:
            status = input(f"{name} [{sid}] - Present? (y/n): ").strip().lower()
            if status in ["y", "n"]:
                break
            print("[ERROR] Please enter only 'y' or 'n'!")
       
        result = "Present" if status == "y" else "Absent"
        attendance_records[sid].append((date_input, result))
   
    print(f"[SUCCESS] Attendance marked for {date_input}!")


def edit_student():
    print("\n--- Edit Student ---")
    while True:
        sid = input("Enter Student ID to edit: ").strip()
        if not is_valid_student_id(sid):
            print("[ERROR] Invalid! Use numbers and hyphens only.")
            continue
        if sid in students:
            break
        print("[ERROR] Student not found!")
        return
   
    while True:
        new_name = input(f"Enter new name for '{students[sid]}': ").strip()
        if not new_name:
            print("[ERROR] Name cannot be empty!")
            continue
        if not is_valid_name(new_name):
            print("[ERROR] Invalid! Use letters only.")
            continue
        break
   
    students[sid] = new_name
    print("[SUCCESS] Student updated!")


def view_all_attendance():
    print("\n" + "="*70)
    print("            STUDENT ATTENDANCE RECORDS")
    print("="*70)
    if not students:
        print("                 No records available.")
    else:
        print(f"{'STUDENT ID':<18} {'NAME':<15} {'DATE':<12} {'STATUS'}")
        print("-"*70)
        for sid, name in students.items():
            if not attendance_records[sid]:
                print(f"{sid:<18} {name:<15} {'---':<12} No record yet")
            else:
                for date, status in attendance_records[sid]:
                    print(f"{sid:<18} {name:<15} {date:<12} {status}")
    print("="*70)


def teacher_menu():
    while True:
        print("\n===== Teacher =====")
        print("1] add student")
        print("2] mark students attendance")
        print("3] edit student")
        print("4] view student attendance records")
        print("5] exit")
       
        choice = input("\nEnter choice: ")
       
        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            edit_student()
        elif choice == "4":
            view_all_attendance()
        elif choice == "5":
            print("Returning to Main Menu...")
            break
        else:
            print("[ERROR] Invalid choice! Enter 1-5.")


# ========== STUDENT FUNCTIONS ==========
def student_view_attendance():
    print("\n--- View My Attendance ---")
    while True:
        sid = input("Enter your Student ID: ").strip()
        if not is_valid_student_id(sid):
            print("[ERROR] Invalid! Use numbers and hyphens only.")
            continue
        if sid in students:
            break
        print("[ERROR] Student ID not found!")
        return
   
    print("\n" + "="*55)
    print(f"     ATTENDANCE FOR: {students[sid]}")
    print("="*55)
    if not attendance_records[sid]:
        print("         No attendance records yet.")
    else:
        print(f"{'DATE':<12} {'STATUS'}")
        print("-"*30)
        for date, status in attendance_records[sid]:
            print(f"{date:<12} {status}")
    print("="*55)


def student_menu():
    while True:
        print("\n===== Student =====")
        print("1] view attendance")
        print("2] exit")
       
        choice = input("\nEnter choice: ")
       
        if choice == "1":
            student_view_attendance()
        elif choice == "2":
            print("Returning to Main Menu...")
            break
        else:
            print("[ERROR] Invalid choice! Enter 1-2.")


# ========== MAIN MENU ==========
def main():
    while True:
        print("\n===== ATTENDANCE SYSTEM =====")
        print("[1] Teacher")
        print("[2] Student")
        print("[3] Exit")
       
        choice = input("\nEnter choice: ")
       
        if choice == "1":
            teacher_menu()
        elif choice == "2":
            student_menu()
        elif choice == "3":
            print("Thank you! Goodbye.")
            break
        else:
            print("[ERROR] Invalid choice! Enter 1-3.")


# Run the system
if __name__ == "__main__":
    main()

