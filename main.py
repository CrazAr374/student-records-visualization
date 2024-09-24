import matplotlib.pyplot as plt
from tabulate import tabulate

students = []
def add_student():
    rollno = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks_obtained = int(input("Enter Marks Obtained: "))
    remarks = input("Enter Remarks: ")
    
    student = {
        'rollno': rollno,
        'name': name,
        'marks_obtained': marks_obtained,
        'remarks': remarks
    }
    students.append(student)

def fetch_students():
    return students

def display_table():
    students = fetch_students()
    headers = ["Roll Number", "Name", "Marks Obtained", "Remarks"]
    table = [[student['rollno'], student['name'], student['marks_obtained'], student['remarks']] for student in students]
    print("\nStudent Records:")
    print(tabulate(table, headers, tablefmt="grid"))

def plot_marks():
    students = fetch_students()
    rollnos = [student['rollno'] for student in students]
    marks = [student['marks_obtained'] for student in students]
    
    plt.figure(figsize=(10, 6))
    plt.bar(rollnos, marks, color='skyblue')
    plt.xlabel('Roll Number')
    plt.ylabel('Marks Obtained')
    plt.title('Marks Obtained by Students')
    plt.xticks(rollnos)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main():
    while True:
        print("\n1. Add Student")
        print("2. Display Table")
        print("3. Plot Marks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_table()
        elif choice == '3':
            plot_marks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
