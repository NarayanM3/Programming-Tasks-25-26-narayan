"""
TASK: 02 Dice Roll

# Skills: RNG, Loops
Simulate rolling a six-sided die X number of times:
Print each roll, store all values in a list of updated totals for each number (56 ones for example):
Allow the user to print:
- Totals for each side
- average dice roll
- Counts for each of the 6 sides
- Extend (look up how to use mathplotlib and produce a bar graph for all of the statistics)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random
import matplotlib.pyplot as plt


def main():
    rolls = int(input("How many times do you want to roll the dice? "))

    results = []
    totals = [0, 0, 0, 0, 0, 0]

    for i in range(rolls):
        roll = random.randint(1, 6)
        results.append(roll)
        totals[roll - 1] += 1
        print("Roll:", roll)

    print("Totals for each side:", totals)

    average = sum(results) / len(results)
    print("Average dice roll:", average)

    print("Counts for each side:")

    for i in range(6):
        print(i + 1, ":", totals[i])

    sides = [1, 2, 3, 4, 5, 6]

    plt.bar(sides, totals)
    plt.xlabel("Dice Side")
    plt.ylabel("Number of Rolls")
    plt.title("Dice Roll Results")
    plt.xticks(sides)
    plt.show()


if __name__ == "__main__":
    main()
