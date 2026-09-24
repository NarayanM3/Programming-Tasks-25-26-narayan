"""
TASK: 01 Csv Writer

# Skills: CSV writing
CAsk the user for:
- Name
- age
- favourite colour
- anything you want
Append this to a CSV file (Extend: allow user to choose to edit the file and read the file)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import csv


def main():
    choice = input("Do you want to append, read, or edit the CSV file? ").lower()
    if choice == "append":
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        favourite_colour = input("Enter your favourite colour: ")
        extra = input("Enter anything else you want to add: ")

        with open("data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, favourite_colour, extra])
            print("Data appended to CSV file.")

    elif choice == "read":
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    elif choice == "edit":
        rows = []
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for i in range(len(list(reader))):
                rows.append(next(reader))

            number = int(input("Enter the row number you want to edit: "))
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            favourite_colour = input("Enter your favourite colour: ")
            extra = input("Enter anything else you want to add: ")
            rows[number] = [name, age, favourite_colour, extra]

            with open("data.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
                print("Data edited in CSV file.")

    else:
        print("Invalid choice. Please choose 'append', 'read', or 'edit'.")


if __name__ == "__main__":
    main()
