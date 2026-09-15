"""
TASK: 06 Simple Login

# Skills: Selection, string comparison
Start with a correct username/password (extend if saved in a text file separately):
- Ask for login
- Print "Welcome" or "Access Denied {number} attempts remaining"
Only allow 3 attempts and close the file

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    attempts = 5

    while attempts > 0:
        entered_username = input("Enter username: ")
        entered_password = input("Enter password: ")

        if entered_username == username and entered_password == password:
            print("Welcome")
            break
        else:
            attempts -= 1
            print("Access Denied. attempts remaining: ", attempts)

    if attempts == 0:
        print("No attempts remaining.")


if __name__ == "__main__":
    main()
