tasks = []

while True:
    print("\n==============================")
    print("       Welcome to Schedify      ")
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
            print("\nNo tasks yet.")
        else:
            print("\n--- ALL TASKS ---")
            for i, t in enumerate(tasks, start=1):
                print(f"\nTask #{i}")
                print(f"Description : {t[0]}")
                print(f"Deadline    : {t[1]}")
                print(f"Category    : {t[2]}")
                print(f"Status      : {t[3]}")
                print("------------------------------")

    # 3. Mark Task as Done
    elif choice == "3":
        if not tasks:
            print("\nNo tasks to mark.")
        else:
            try:
                num = int(input("Enter task number to mark as done: "))
                if 1 <= num <= len(tasks):
                    if tasks[num-1][3] == "Done":
                        print("\nTask is already marked as Done.")
                    else:
                        tasks[num-1][3] = "Done"
                        print("\nTask marked as Done!")
                else:
                    print("\nInvalid task number.")
            except ValueError:
                print("\nPlease enter a valid number.")

    # 4. Update/Delete Task
    elif choice == "4":
        if not tasks:
            print("\nNo tasks available.")
        else:
            try:
                num = int(input("Enter task number: "))
                if 1 <= num <= len(tasks):
                    choice2 = input("Update (U) or Delete (D)?: ").upper()

                    if choice2 == "U":
                        new_desc = input("New description (leave blank to keep current): ")
                        new_date = input("New deadline (leave blank to keep current): ")
                        new_cat = input("New category (leave blank to keep current): ")

                        if new_desc:
                            tasks[num-1][0] = new_desc
                        if new_date:
                            tasks[num-1][1] = new_date
                        if new_cat:
                            tasks[num-1][2] = new_cat

                        print("\nTask updated successfully!")

                    elif choice2 == "D":
                        tasks.pop(num-1)
                        print("\nTask deleted successfully!")

                    else:
                        print("\nInvalid option.")
                else:
                    print("\nInvalid task number.")
            except ValueError:
                print("\nPlease enter a valid number.")

    # 5. Task Summary
    elif choice == "5":
        total = len(tasks)
        pending = sum(1 for t in tasks if t[3] == "Pending")
        done = sum(1 for t in tasks if t[3] == "Done")

        print("\n--- TASK SUMMARY ---")
        print(f"Total Tasks    : {total}")
        print(f"Pending Tasks  : {pending}")
        print(f"Completed Tasks: {done}")

        if total > 0:
            percent = (done / total) * 100
            print(f"Completion Rate: {percent:.2f}%")
        else:
            print("Completion Rate: 0%")

    # 6. Exit
    elif choice == "6":
        print("\nThank you for using Schedify.")
        break

    else:
        print("\nInvalid choice. Try again.")
