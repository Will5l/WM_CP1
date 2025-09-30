# WM 2nd List Manager

# FL class Shopping List Manager

the_list = []

while True:
    action = input("1. Add task\n2. Mark task done\n3. Show list\n4. Remove task from list\n5. Exit\n")
    #Write your code here
    if action == "1":
        task = input("Enter the task: ")
        the_list.append(task)
        print(f"{task} has been added.")
    elif action == "2":
        task = input("What task would you like to mark as done? ")
        if task in the_list:
            location = the_list.index(task)
            print(location)
            print(f"{task} was marked as done")
            the_list.remove(task)
            the_list.insert(location, f"\033[9m{task}\033[0m")
        else:
            print("Item was not found")
    elif action == "3":
        if the_list:
            for i, task in enumerate(the_list, 1):
                print(f"{i}. {task}")
    elif action == "4":
        task = input("What task would you like to remove?")
        if task in the_list:
            the_list.remove(task)
            print(f"{task} removed from list")
        elif  f"\033[9m{task}\033[0m" in the_list:
            the_list.remove(f"\033[9m{task}\033[0m")
            print(f"{task} removed from the list")
        else:
            print("Task not found")
    elif action == "5":
        break
    else:
        print("Invalid choice")