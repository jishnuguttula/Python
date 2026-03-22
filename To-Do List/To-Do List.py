tasks = []

while True:
    print("1.Add Task 2.View 3.Remove 4.Exit")
    ch = int(input())

    if ch == 1:
        task = input("Enter task: ")
        tasks.append(task)

    elif ch == 2:
        for t in tasks:
            print(t)

    elif ch == 3:
        task = input("Enter task to remove: ")
        tasks.remove(task)

    else:
        break