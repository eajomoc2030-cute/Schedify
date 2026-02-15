tasks = []

while True:
    print("\n==============================")
    print("        Welcome to Schedify        ")
    print("==============================")
    print("Note: When entering dates, use the format MM-DD-YYYY")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Update/Delete Task")
    print("5. View Task Summary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # 1. Add Task
    if choice == "1":
        print("\n--- Add a New Task ---")
        desc = input("Enter task description: ")
        date = input("Enter deadline (MM-DD-YYYY): ")
        cat = input("Category (Academic/Non-Academic): ")
        
        tasks.append([desc, date, cat, "Pending"])
        print("\nTask added successfully!")

    # 2. View Tasks
    elif choice == "2":
        if not tasks:
            print("\nNo tasks available.")
        else:
            print("\n--- ALL TASKS ---")
            for i, task in enumerate(tasks, start=1):
                print(f"\nTask #{i}")
                print(f"Description : {task[0]}")
                print(f"Deadline    : {task[1]}")
                print(f"Category    : {task[2]}")
                print(f"Status      : {task[3]}")
                print("------------------------------")

    # 3. Mark Task as Done
    elif choice == "3":
        if not tasks:
            print("\nNo tasks available.")
        else:
            try:
                num = int(input("Enter task number to mark as done: "))
                if 1 <= num <= len(tasks):
                    if tasks[num - 1][3] == "Done":
                        print("\nTask is already marked as Done.")
                    else:
                        tasks[num - 1][3] = "Done"
                        print("\nTask marked as Done successfully.")
                else:
                    print("\nInvalid task number.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")

    # 4. Update/Delete Task
    elif choice == "4":
        if not tasks:
            print("\nNo tasks available.")
        else:
            try:
                num = int(input("Enter task number: "))
                if 1 <= num <= len(tasks):
                    action = input("Update (U) or Delete (D)?: ").upper()

                    if action == "U":
                        print("\n--- Update Task ---")
                        new_desc = input("New description (leave blank to keep current): ")
                        new_date = input("New deadline (leave blank to keep current): ")
                        new_cat = input("New category (leave blank to keep current): ")

                        if new_desc:
                            tasks[num - 1][0] = new_desc
                        if new_date:
                            tasks[num - 1][1] = new_date
                        if new_cat:
                            tasks[num - 1][2] = new_cat

                        print("\nTask updated successfully.")

                    elif action == "D":
                        tasks.pop(num - 1)
                        print("\nTask deleted successfully.")

                    else:
                        print("\nInvalid option selected.")

                else:
                    print("\nInvalid task number.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")

    # 5. Task Summary
    elif choice == "5":
        total = len(tasks)
        pending = sum(1 for task in tasks if task[3] == "Pending")
        completed = sum(1 for task in tasks if task[3] == "Done")

        print("\n--- TASK SUMMARY ---")
        print(f"Total Tasks    : {total}")
        print(f"Pending Tasks  : {pending}")
        print(f"Completed Tasks: {completed}")

        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"Completion Rate: {completion_rate:.2f}%")
        else:
            print("Completion Rate: 0%")

    # 6. Exit
    elif choice == "6":
        print("\nThank you for using Schedify.")
        break

    else:
        print("\nInvalid choice. Please try again.")
