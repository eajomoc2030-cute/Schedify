tasks = []

while True:
    print("\n==============================")
    print("       Welcome to Schedify      ")
    print("==============================")
    print("Note: When entering dates, use the format MM-DD-YYYY (with dashes)")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Update/Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")

    # 1. Add task
    if choice == "1":
        print("\n--- Add a New Task ---")
        desc = input("Enter task description: ")
        date = input("Enter deadline (MM-DD-YYYY): ")
        cat = input("Category (Academic/Non-Academic): ")
        tasks.append([desc, date, cat, "Pending"])
        print("\nTask added successfully!")
        print(f"Task: {desc}")
        print(f"Deadline: {date}")
        print(f"Category: {cat}")
        print("------------------------------")

    # 2. View tasks 
    elif choice == "2":
        if len(tasks) == 0:
            print("\nNo tasks yet.")
        else:
                print("\n--- TASKS ---")
        
        # a. Print Pending Tasks
        print("\n--- PENDING TASKS ---")
        pending_count = 0
        for i, t in enumerate(tasks, start=1):
            if t[3] == "Pending":
                print(f"\nTask #{i} (Pending)")
                print(f"Description : {t[0]}")
                print(f"Deadline    : {t[1]}")
                print(f"Category    : {t[2]}")
                print("------------------------------")
                pending_count += 1
        
        if pending_count == 0:
            print("No tasks pending!")

        # b. Print Done Tasks
        print("\n--- COMPLETED TASKS ---")
        done_count = 0
        for i, t in enumerate(tasks, start=1):
            if t[3] == "Done":
                print(f"Task #{i} (Done)")
                print(f"Description : {t[0]}")
                print(f"Deadline    : {t[1]}")
                print(f"Category    : {t[2]}")
                print("------------------------------")
                done_count += 1
        
        if done_count == 0:
            print("No tasks completed yet.")
            
    # 3. Mark task as done
    elif choice == "3":
        if len(tasks) == 0:
            print("\nNo tasks to mark.")
        else:
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(tasks):
                if tasks[num-1][3] == "Done":
                    print("\nTask is already marked as Done.")
                else:
                    tasks[num-1][3] = "Done"
                    print("\nTask marked as Done. Keep it up!")
                    print(f"Task: {tasks[num-1][0]}")
            else:
                print("\nInvalid task number.")

    # 4. Update / delete task
    elif choice == "4":
        if len(tasks) == 0:
            print("\nNo tasks to update or delete.")
        else:
            num = int(input("Enter task number to update/delete: "))
            if 1 <= num <= len(tasks):
                choice2 = input("Update (U) or Delete (D)?: ").upper()

                if choice2 == "U":
                    print("\n--- Update Task ---")
                    print("Note: Enter date in MM-DD-YYYY format (with dashes)")
                    new_desc = input(f"New description (leave blank to keep '{tasks[num-1][0]}'): ")
                    new_date = input(f"New deadline (leave blank to keep '{tasks[num-1][1]}'): ")
                    new_cat = input(f"New category (leave blank to keep '{tasks[num-1][2]}'): ")

                    if new_desc: tasks[num-1][0] = new_desc
                    if new_date: tasks[num-1][1] = new_date
                    if new_cat: tasks[num-1][2] = new_cat

                    print("\nTask updated successfully!")
                    print(f"Task #{num} now:")
                    print(f"Description : {tasks[num-1][0]}")
                    print(f"Deadline    : {tasks[num-1][1]}")
                    print(f"Category    : {tasks[num-1][2]}")
                    print(f"Status      : {tasks[num-1][3]}")

                elif choice2 == "D":
                    print(f"\nDeleting Task: {tasks[num-1][0]}")
                    tasks.pop(num-1)
                    print("Task deleted successfully!")

                else:
                    print("\nInvalid option.")
            else:
                print("\nInvalid task number.")

    # 5. Exit
    elif choice == "5":
        print("Thank you for using Schedify.")
        break

    else:
        print("\nInvalid choice. Try again.")
