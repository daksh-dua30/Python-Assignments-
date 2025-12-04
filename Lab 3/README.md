📚 Library Inventory Manager — Python Mini Project

A command-line based Library Management System built using Object-Oriented Programming (OOP) in Python.
The project allows library staff to add, issue, return, search and view books, while saving data persistently using JSON.

🚀 Features

✔ Add new books to catalog
✔ Issue and return books
✔ Search books by title / ISBN
✔ Display complete inventory
✔ Automatic JSON file persistence
✔ Exception handling and logging
✔ Fully modular folder structure using Python packages

🏗 Folder Structure
library-inventory-manager/
│
├─ library_manager/
│   ├─ __init__.py
│   ├─ book.py
│   ├─ inventory.py
│
├─ cli/
│   ├─ main.py
│
├─ catalog.json
├─ requirements.txt
└─ README.md

🔧 Technologies & Concepts Used
Concept / Module	Description
Python OOP	Classes, objects, encapsulation
File Handling	Persistent storage using JSON file
Exception Handling	try/except blocks for error safety
Logging	Error & activity logs saved using logging module
CLI Interaction	Menu-driven interface
Python Packaging	__init__.py and modular imports
▶️ How to Run the Project
1️⃣ Install Python (if not installed)

https://www.python.org/downloads/

2️⃣ Navigate to project folder
cd library-inventory-manager

3️⃣ Run the CLI program
python cli/main.py

📌 Usage Demo

When the program runs, it shows this menu:

===== LIBRARY INVENTORY MANAGER =====
1. Add Book
2. Issue Book
3. Return Book
4. View All Books
5. Search Book
6. Exit


Enter a choice number and follow on-screen instructions.

📦 Project Requirements

The following dependencies are included in requirements.txt:

json
pathlib
logging


No external libraries are required — runs on standard Python.

🧪 (Optional) Unit Tests

Unit test support can be added inside a /tests/ folder using:

pytest or unittest


🧑‍💻 Author

 Daksh Dua
 
Course: Programming for Problem Solving using Python

Institution: K.R. Mangalam University
