"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


def calculate_average(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)


def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'q' to finish): ")
        if user_input.lower() == "q":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers


def main():
    print("Average Calculator!")
    numbers = get_numbers()
    average = calculate_average(numbers)
    if average is None:
        print("no numbers.")
    else:
        print("numbers entered - ", numbers)
        print("average - ", average)


if __name__ == "__main__":
    main()
