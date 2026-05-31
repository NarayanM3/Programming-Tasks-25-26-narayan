"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random


def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1


def main():
    numbers = []
    for i in range(10):
        numbers.append(random.randint(1, 1000))
    print("numbers generated - ", numbers)
    target = int(input("Enter a number to search for: "))
    answer = linear_search(numbers, target)
    if answer == -1:
        print("number not found.")
    else:
        print("number found at index - ", answer)


if __name__ == "__main__":
    main()
