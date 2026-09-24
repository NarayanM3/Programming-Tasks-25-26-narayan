"""
TASK: 04 Temp Stats Csv

# Skills CSV read, simple maths
Go to this site https://www.metoffice.gov.uk/hadobs/hadcet/data/download.html and download the txt file
Daily Mean Temperature.
This file has dates and daily temperatures:
- Read all of the values
- Find the highest, lowest and average
- Print those three values
Extend - See how you can potentially use the dates to chart daily temp changes by years, by months
by day comparisons over time. Maybe chart them using mathplotlib or another library. Just see what you can do with it

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import os
import matplotlib.pyplot as plt

def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(folder, "meantemp_daily_totals.txt")

    dates = []
    temperatures = []

    with open(filename, "r") as file:
        for line in file:
            data = line.split()

            try:
                temperature = float(data[1])
                dates.append(data[0])
                temperatures.append(temperature)
            except (ValueError, IndexError):
                continue

    highest = max(temperatures)
    lowest = min(temperatures)
    average = sum(temperatures) / len(temperatures)

    print("Highest temperature:", highest)
    print("Lowest temperature:", lowest)
    print("Average temperature:", average)

    plt.plot(dates, temperatures)
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.title("Daily Mean Temperature")
    plt.show()


if __name__ == "__main__":
    main()