Python phonebook project structure and instructions in English:

📂 Project Structure

simple-phonebook-python/
├── src/
│   └── phonebook/
│       ├── __init__.py
│       └── core.py
├── tests/
│   └── test_phonebook.py
├── run.py
├── README.md
├── pyproject. toml
└── .gitignore

🔹 Explanation:

* src/phonebook/core.py → Main phonebook logic
* run.py → Main script to run the program
* tests/ → Test files for your phonebook functions
* README.md → Project description
* .gitignore → Ignore unnecessary files/folders
* pyproject.toml → Project info & dependencies

🧩 Step 1: Create folders and files

mkdir -p src/phonebook
mkdir tests
touch src/phonebook/__init__.py
touch src/phonebook/core.py
touch tests/test_phonebook.py
touch run.py
touch README.md
touch pyproject. toml
touch .gitignore

✅ Folders are ready 📂

🧩 Step 2: Core module

src/phonebook/core.py

contacts = []

def add_contact(name: str, phone: str):
    contacts. append({"name": name, "phone": phone})

def get_contacts():
    return contacts

def search_contact(search_name: str):
    return [
        contact for contact in contacts
        if search_name.lower() in contact['name'].lower()
    ]


🧩 Step 3: Main run file

from phonebook.core import add_contact, get_contacts, search_contact

def main():
    while True:
        print("🌟 Phonebook 🌟")
        print("1️⃣ Add Contact")
        print("2️⃣ Show Contacts")
        print("3️⃣ Search by Name")
        print("4️⃣ Exit")
        choice = input("Your choice: ")
        
        if choice == "1":
            name = input("👤 Name: ")
            phone = input("📞 Phone Number: ")
            add_contact(name, phone)
            print(f"✅ {name} has been added successfully!\n")
        elif choice == "2":
            contacts = get_contacts()
            print("\n📋 Contact List")
            if not contacts:
                print("⚠️ No contacts found.\n")
            else:
                for i, c in enumerate(contacts, start=1):
                    print(f"{i}. 👤 {c['name']} | 📞 {c['phone']}")
            print()
        elif choice == "3":
            search_name = input("👤 Enter name to search: ")
            results = search_contact(search_name)
            if results:
                for c in results:
                    print(f"✅ Found: 👤 {c['name']} | 📞 {c['phone']}")
            else:
                print("❌ Contact not found.\n")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()


🧩 Step 4: Tests

tests/test_phonebook.py

from phonebook. core import add_contact, get_contacts, search_contact

def test_add_and_get():
    add_contact("Ali", "12345")
    add_contact("Sara", "67890")
    contacts = get_contacts()
    assert len(contacts) == 2

def test_search():
    add_contact("John", "11111")
    results = search_contact("John")
    assert len(results) == 1
    assert results[0]["phone"] == "11111"


🧩 Step 5: pyproject. toml

[project]
name = "simple-phonebook"
version = "0.1.0"
description = "A simple interactive phonebook with emojis in Python"
authors = [{ name = "Your Name" }]
readme = "README.md"
requires-python = ">=3.8"

[tool.pytest.ini_options]
pythonpath = ["src"]

🧩 Step 6: .gitignore

__pycache__/
*.pyc
.venv/
.env

🧩 Step 7: Run tests
pip install pytest
pytest

Your professional Python Phonebook project with CI/CD explained in English:

🚀 Take Your Phonebook Project to Professional CI/CD

Every time you push code or open a pull request, your tests will run automatically 🧪

🧩 Step 1: Create GitHub Actions folder 📂
In your project root, run:

mkdir -p .github/workflows
touch .github/workflows/python-tests.yml

🧩 Step 2: Write the Workflow 🧠

File: .github/workflows/python-tests.yml

name: Python CI Tests 🐍

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository 📥
        uses: actions/checkout@v4

      - name: Set up Python 🐍
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install dependencies ⚙️
        run: |
          python -m pip install --upgrade pip
          pip install pytest

      - name: Run tests 🧪
        run: pytest

📌 Explanation

* Triggers on push or pull request to the main branch

* Runs on Ubuntu + Python 3.10

* Installs pytest and runs all tests in tests/ automatically ✅

🧩 Step 3: Push Workflow to GitHub ☁️

git add .github/workflows/python-tests.yml
git commit -m "Add GitHub Actions CI for automatic tests."
git push


🎯 Outcome

Your Phonebook project now has:
📁 Standard structure
🧪 Automated tests
🤖 Professional CI


# Simple Phonebook with Emojis 🌟📞

A simple **interactive phonebook** implemented in Python with **emojis**, designed for learning Python, testing, and standard project structure.  
Supports adding, viewing, and searching contacts.

---

## 🚀 Features
- Add new contacts 📝
- Show all contacts 📋
- Search contacts by name 🔍
- Interactive terminal-based interface
- Standard Python package structure 📁
- Automated tests with pytest 🧪
- Continuous Integration with GitHub Actions 🤖

---

## 🧩 Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/simple-phonebook-python.git
cd simple-phonebook-python

Install dependencies (if any):
pip install -r requirements.txt  # optional

▶️ How to Run
python run.py

You'll see an interactive menu:
🌟 Phonebook 🌟
1️⃣ Add Contact
2️⃣ Show Contacts
3️⃣ Search by Name
4️⃣ Exit


📌 Example Usage

Adding a contact:
1
👤 Name: Ali
📞 Phone Number: 12345
✅ Ali has been added successfully!

Viewing contacts:
2
📋 Contact List
1. 👤 Ali | 📞 12345

Searching for a contact:
3
👤 Enter name to search: Ali
✅ Found: 👤 Ali | 📞 12345

🧪 Running Tests
pytest

All tests are located in the tests/ folder.

🤖 Continuous Integration

GitHub Actions automatically runs all tests on every push or pull request to the main branch.
This ensures code quality and prevents regressions.

📄 Project Structure
simple-phonebook-python/
├── src/phonebook/      # Core logic
├── tests/              # Automated tests
├── run.py              # Entry point
├── README.md           # This file
├── pyproject.toml      # Project config
└── .gitignore

🎯 Use Cases
* Learning Python and basic OOP concepts
* Practicing testing with pytest
* Understanding standard project structure
* CI/CD workflow with GitHub Actions

📄 License

This project is open-source and free to use for educational purposes.

---

### ✅ Next Step
Add this README to your repo:

```bash
git add README.md
git commit -m "Add professional README in English with examples."
git push


