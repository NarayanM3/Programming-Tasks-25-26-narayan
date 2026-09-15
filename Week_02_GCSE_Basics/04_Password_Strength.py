"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def get_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        strength += 1
    if any(not char.isalnum() for char in password):
        strength += 1

    if strength == 4:
        return "strong"
    elif strength == 3:
        return "medium"
    else:
        return "weak"


def main():
    password = input("Enter a password: ")
    strength = get_password_strength(password)
    print("Password strength: ", strength)


if __name__ == "__main__":
    main()
