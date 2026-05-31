"""
TASK: 06 Temperature Converter

# Temperature Converter
Build a converter tool:
- Convert Celsius <-> Fahrenheit.
- Provide a looped menu.
- Validate user input.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def main():
    choice = " "
    while choice.lower() != "q":
        print("Temperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("Q. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(str(celsius) + "°C is " + str(fahrenheit) + "°F")
            except ValueError:
                print("Invalid input")
        elif choice == "2":
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = (fahrenheit - 32) * 5 / 9
                print(str(fahrenheit) + "°F is " + str(celsius) + "°C")
            except ValueError:
                print("Invalid input")
        elif choice.lower() == "q":
            print("bye bye!")
        else:
            print("Invalid option. Please choose 1, 2, or Q.")


if __name__ == "__main__":
    main()
