"""
TASK: 02 Times Tables

# Skills: Loops,input validation
Ask the user for a number, print the multiplication from 1 to 12 in a readable format:

Extend by using a function you can call for easy entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random


def main():
    table = int(input("Enter the times table you want to be tested on: "))
    for i in range(12):
        number = random.randint(1, 12)
        answer = number * table
        user_answer = int(input(str(number) + " x " + str(table) + " = "))

        if user_answer == answer:
            print("Correct!")
        else:
            print("Incorrect. The answer is:", answer)


if __name__ == "__main__":
    main()
