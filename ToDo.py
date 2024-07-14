tasks = []
print("Welcome to your day organiser!!")

def addtask():
    task = input("What do you want to add? ")
    tasks.append(task)
    print(f"Task '{task}' added 😊")

def listask():
    print("\n")
    if tasks:
        print("Your today's tasks are:")
        for index, task in enumerate(tasks):
            print(f"Task {index+1}. {task}")
    else:
        print("No tasks added yet.")

def deletetask():
    listask()
    if tasks:  # Check if there are tasks to delete
        try:
            taskToDelete = int(input("Enter task number to delete: ")) - 1
            if 0 <= taskToDelete < len(tasks):
                deleted_task = tasks.pop(taskToDelete)
                print(f"Task '{deleted_task}' has been deleted.")
            else:
                print("Invalid task number, please try again!")
        except ValueError:
            print("Invalid input, please enter a valid number!")
    else:
        print("No tasks to delete.")

while True:
    print("\nWhat do you want to do (●'◡'●)")
    print("-----------------------------------")
    print("1. Add a task.")
    print("2. Delete a task.")
    print("3. Show your tasks.")
    print("4. Quit.")
    
    try:
        choice = (input("Enter your choice: ").strip())
        if choice == '1':
            addtask()
        elif choice == '2':
            deletetask()
        elif choice == '3':
            listask()
        elif choice == '4':
            print("Thanks 🌟")
            print("Goodbye👋👋")
            break
        else:
            print("Invalid choice 😢")
    except ValueError:
        print("Invalid input, please enter a number between 1 and 4.")
