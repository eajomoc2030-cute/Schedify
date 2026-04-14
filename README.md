# Schedify

**Schedify** is a simple and user-friendly task organizer designed for students.  
It helps manage academic responsibilities and personal activities in one place, making it easier to record, organize, and track tasks over time.

Research in cognitive psychology shows that working memory has a limited capacity, and individuals often rely on external memory aids to manage information more effectively. These external representations help reduce cognitive load and support task organization (Zhang & Wang, 2009). Studies on task management also show that people use to-do lists to record, organize, and track tasks over time, making them an important tool for supporting task completion (Bellotti et al., 2004).

Based on these findings, Schedify was developed as a lightweight system to support structured task management in a simple and accessible way for students.

---

## Features

- Add Task – Create tasks with description, deadline, and category  
- View Tasks – Display all saved tasks in order  
- Mark Task as Done – Update task status to completed  
- Update/Delete Task – Modify or remove existing tasks  
- View Task Summary – Show total, pending, and completed tasks with completion rate  

---

## Technologies Used

- Python 3 – Simple and beginner-friendly programming language  
- Command-Line Interface (CLI) – Lightweight system interface  

No external libraries were used.

---

## How to Run

### OPTION 1: Run Online
1. Open the Python file: [Schedify](https://onlinegdb.com/4D7dwqhFXF)  
2. Click Run  
3. Use the menu:
   1. Add Task  
   2. View Tasks  
   3. Mark Task as Done  
   4. Update/Delete Task  
   5. View Task Summary  
   6. Exit  
4. Enter the number of your chosen option  
5. Use MM-DD-YYYY format for deadlines  

---

### OPTION 2: Run Locally
1. Install Python 3  
2. Download or clone the repository  
3. Open terminal in project folder  
4. Run:
   python schedify.py  
5. Use the same menu options  

---

## Methodology

Schedify uses a simple menu-based system built in Python.

### How the Main Features Work
- Add Task – Stores task details in a structured list  
- View Tasks – Displays all tasks in order of entry  
- Mark Task as Done – Updates task status from pending to completed  
- Update/Delete Task – Allows editing or removal using task index  
- View Task Summary – Calculates total, pending, and completed tasks  

### System Structure
Schedify is a standalone command-line application where all logic is handled within a single Python file.

---

## Design Decisions

- Tasks remain in insertion order for clarity  
- No autosave feature to maintain simplicity  
- No external libraries used  
- Focus is on core functionality and usability  
- Designed specifically for student task management  

---

## Current Status

Version 1.3.0 – Stable  
Core task management features fully implemented  

---

## Programming and Computing Ethics

- No personal or sensitive data is collected  
- All tasks exist only during runtime  
- No external data sharing occurs  
- Designed for educational use only  

---

## Benefits

- Improves task organization  
- Supports time management  
- Reduces cognitive overload  
- Encourages responsibility and discipline  
- Helps students track academic workload  

---

## Members

- Erolyn Jomoc  
- Eden Conales  
- Kaira Bibera  

---

## License

This project is for educational purposes only.

---

## Development Note

This project was developed by the group members. ChatGPT was used as an assistive tool to help improve grammar, clarify explanations, and refine documentation structure. All content was reviewed, understood, and edited by the group before submission.

---

## References

Bellotti, V., Dalal, B., Good, N., Flynn, P., Bobrow, D. G., & Ducheneaut, N. (2004). *What a to-do: Studies of task management towards the design of a personal task list manager*. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI ’04). https://doi.org/10.1145/985692.985785  

Zhang, J., & Wang, H. (2009). *An exploration of the relations between external representations and working memory*. PLOS ONE, 4(8), e6513. https://doi.org/10.1371/journal.pone.0006513
