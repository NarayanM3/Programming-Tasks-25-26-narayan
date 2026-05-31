"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random


def reverse_list(values):
    reversed_list = []
    for i in range(len(values) - 1, -1, -1):
        reversed_list.append(values[i])
    return reversed_list


def main():
    numbers = []
    for i in range(10):
        numbers.append(random.randint(1, 1000))
        reversed_numbers = reverse_list(numbers)
    print("original list - ", numbers)
    print("reversed list - ", reversed_numbers)


if __name__ == "__main__":
    main()
