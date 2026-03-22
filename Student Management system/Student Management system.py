students = {}

def add_student():
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

def display():
    for name, marks in students.items():
        print(name, marks)

def topper():
    top = max(students, key=students.get)
    print("Topper:", top, students[top])

while True:
    print("1.Add 2.Display 3.Topper 4.Exit")
    ch = int(input())

    if ch == 1:
        add_student()
    elif ch == 2:
        display()
    elif ch == 3:
        topper()
    else:
        break