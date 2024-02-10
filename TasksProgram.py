tasks = []
con = False

def welcome():
    global con
    print("Welcome to our program. You can:")
    print("1. Add tasks")
    print("2. Remove tasks")
    print("3. Mark tasks as done")
    print("4. See your tasks")
    print("5. Clear the task list")
    print("6. Close the program")
    
    while True:
        f1 = input("Enter your choice: ")
        if f1 not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid input. Please try again.")
        elif f1 == '1':
            con = True
            add()
        elif f1 == '2':
            if not con:
                print("You need to add tasks first.")
            else:
                remove()
        elif f1 == '3':
            if not con:
                print("You need to add tasks first.")
            else:
                done()
        elif f1 == '4':
            if not con:
                print("You need to add tasks first.")
            else:
                show_tasks()
        elif f1 == '5':
            if not con:
                print("You need to add tasks first.")
            else:
                clear_tasks()
        elif f1 == '6':
            print("Closing the program...")
            exit()

def add():
    while True:
        x = input("Enter your task for today: ")
        tasks.append(x)
        y = input("Do you want to add more tasks? (Y/N): ").lower()
        if y not in ['y', 'n']:
            print("Invalid input. Please enter 'Y' or 'N'.")
        elif y == 'n':
            welcome()

def remove():
    if len(tasks) == 0:
        print("The task list is empty.")
        welcome()
    print_tasks()
    while True:
        x = int(input("Enter the number of the task you would like to remove: ")) - 1
        if x < 0 or x >= len(tasks):
            print("Invalid task number. Please try again.")
        else: 
            tasks.pop(x)
            print("The task has been removed.")
            break
    while True:
        y = input("Do you want to remove more tasks? (Y/N): ").lower()
        if y == 'y':
            remove()
        elif y == 'n':
            welcome()
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def done():
    if len(tasks) == 0:
        print("The task list is empty.")
        welcome()
    print_tasks()
    while True:
        x = int(input("Enter the number of the task you have completed: ")) - 1
        if x < 0 or x >= len(tasks):
            print("Invalid task number. Please try again.")
        else: 
            tasks[x] += " (completed)"
            print("The task has been marked as completed.")
            break
    while True:
        y = input("Do you want to mark more tasks as done? (Y/N): ").lower()
        if y == 'y':
            done()
        elif y == 'n':
            welcome()
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def show_tasks():
    if len(tasks) == 0:
        print("The task list is empty.")
        welcome()
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        input("Press Enter to return to the main menu.\n")
        welcome()

def clear_tasks():
    tasks.clear()
    print("The task list has been cleared.")
    welcome()

def print_tasks():
    if len(tasks) == 0:
        print("The task list is empty.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

welcome()
