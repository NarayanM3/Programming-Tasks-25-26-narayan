"""
TASK: 03 Contact Book

# Store contacts in a text file, each line containing
name,phone,email
Program must allow:
- Add contact
- Search contact (sequential search)
- Display all

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
CONTACT_FILE = "contacts.txt"


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    with open(CONTACT_FILE, "a") as file:
        file.write(name + "," + phone + "," + email + "\n")

    print("Contact added.")


def search_contact():
    search_name = input("Enter the name to search for: ")

    try:
        with open(CONTACT_FILE, "r") as file:
            found = False

            for line in file:
                contact = line.strip().split(",")

                if contact[0].lower() == search_name.lower():
                    print("Name:", contact[0])
                    print("Phone:", contact[1])
                    print("Email:", contact[2])
                    found = True
                    break

            if not found:
                print("Contact not found.")

    except FileNotFoundError:
        print("No contacts found.")


def display_all():
    try:
        with open(CONTACT_FILE, "r") as file:
            contacts = file.readlines()

            if len(contacts) == 0:
                print("No contacts found.")
            else:
                for line in contacts:
                    contact = line.strip().split(",")
                    print("Name:", contact[0])
                    print("Phone:", contact[1])
                    print("Email:", contact[2])
                    print()

    except FileNotFoundError:
        print("No contacts found.")


def main():
    while True:
        print("1. Add contact")
        print("2. Search contact")
        print("3. Display all")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            display_all()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()