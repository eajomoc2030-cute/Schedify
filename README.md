# Schedify

**Schedify** is a simple and user-friendly task organizer designed for students.  
It helps manage academic responsibilities and personal activities in one place, making it easy to track deadlines, update tasks, and stay organized.

---

## Features

- **Add Tasks Easily** – Add both academic and non-academic tasks.  
- **Task Details** – Set a description, deadline, and category for each task.  
- **Task Overview** – View all tasks in the order they were added.  
- **Task Status** – Mark tasks as **Pending** or **Done**.  
- **Edit or Delete Tasks** – Update or remove tasks anytime.
- **Task Summary** – View total, pending, and completed tasks with completion percentage.
- **Input Validation** - Prevents errors when invalid numbers are entered. 
- **Beginner-Friendly** – Simple and intuitive interface designed for students.

---

### Technologies Used
- Python 3 – Chosen for its simplicity and beginner-friendly syntax.
- Command-Line Interface (CLI) – Used to keep the system lightweight and focused on functionality.

No external libraries were used to maintain simplicity and clarity of the core logic.


---

## How to Run
### OPTION 1: Run Online
1. Open the Python file: [Schedify](https://onlinegdb.com/y8sIao2-2).
2. Click **Run**
3. The menu will appear:
   1. Add Task
   2. View Tasks
   3. Mark Task as Done
   4. Update/Delete Task
   5. Exit
4. Enter the number of your chosen option.
5. When entering deadlines, use the format: MM-DD-YYYY
6. Continue using the menu until you choose 5 (Exit).

### OPTION 2: Run Locally
1. Make sure Python 3 is installed on your computer/laptop.
2. Download or clone the schedify repository.
3. Open the project folder.
4. Open a terminal or command prompt inside the folder.
5. Run the program using: python schedify.py
6. The menu will appear:
   1. Add Task
   2. View Tasks
   3. Mark Task as Done
   4. Update/Delete Task
   5. Exit
7. Enter the number of your chosen option.
8. When entering deadlines, use the format: MM-DD-YYYY
9. Continue using the menu until you choose 5 (Exit).
    
---

## Methodology
Schedify uses a simple menu-based system built using Python.

## How the Main Features Work
- Add Task – Tasks are saved in a list. Each task includes a description, deadline, category, and status.
- View Tasks – The program displays all tasks in the order they were added.
- Mark as Done – The task status changes from “Pending” to “Done.”
- Update/Delete Task – The user chooses a task number to edit or remove it.
- Task Summary – The program counts total, pending, and completed tasks and shows the percentage completed.
- Input Validation – The program checks user input to avoid errors.

### Backend–Frontend Communication
Not applicable. Schedify is a standalone command-line application where all logic and user interaction occur within a single Python file.

---

## Design Decisions
- The system does not use automatic sorting to keep task order clear.
- No autosave feature is used to maintain simplicity.
- Tasks are shown in the order they were added.
- Advanced features were removed in Version 1.2.0 to make the system easier to use and understand.
- No external libraries were used.

---

## Current Status

Current Version: v1.3.0
The project includes core task management features and improved stability.

---

## Programming and Computing Ethics
This project follows basic programming ethics principles:
   - No personal or sensitive data is collected.
   - Tasks are stored only during program execution.
   - No external data sharing is involved.
   - The system is designed to be simple and accessible for student users.

---

## Benefits
- Helps manage time effectively  
- Reduces stress by keeping tasks organized  
- Improves academic performance through proper planning  
- Encourages responsibility and accountability  

---

## Members
- **Erolyn Jomoc**  
- **Eden Conales**  
- **Kaira Bibera**

---

## License
This project is for **educational purposes only**.

## Development Note
This project was coded by the group members.

We used AI tools to:
- Help explain some parts of the code
- Fix small errors
- Guide us on syntax and how to write certain parts
We made sure we understood the code and edited it ourselves before submitting. :) 

