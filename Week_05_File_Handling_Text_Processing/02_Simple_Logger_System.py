"""
TASK: 02 Simple Logger System

# Create a script that appends time-stamped log entries to a file.
Menu:
- Add Log
- View Log
- Clear Log

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
from datetime import datetime

LOG_FILE = "log.txt"


def add_log():
    message = input("Enter log message: ")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(time + " - " + message + "\n")

    print("Log added.")


def view_log():
    try:
        with open(LOG_FILE, "r") as file:
            contents = file.read()

        if contents:
            print(contents)
        else:
            print("The log is empty.")

    except FileNotFoundError:
        print("The log is empty.")


def clear_log():
    with open(LOG_FILE, "w") as file:
        file.write("")

    print("Log cleared.")


def main():
    while True:
        print("\n1. Add Log")
        print("2. View Log")
        print("3. Clear Log")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_log()
        elif choice == "2":
            view_log()
        elif choice == "3":
            clear_log()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
