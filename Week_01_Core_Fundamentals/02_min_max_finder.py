"""
TASK: 02 Min Max Finder

# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


def find_min_max(values):
    min_value = values[0]
    max_value = values[0]
    for num in values:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    return min_value, max_value


def main():
    numbers = [3, 5, 7, 4, 8, 9, 1]
    minimum, maximum = find_min_max(numbers)
    print("numbers entered - ", numbers)
    print("minimum - ", minimum)
    print("maximum - ", maximum)


if __name__ == "__main__":
    main()
