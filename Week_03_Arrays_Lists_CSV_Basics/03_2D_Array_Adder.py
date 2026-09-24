"""
TASK: 03 2D Array Adder

# 2D Array Added
Create a 2D arraw and allow user to:
- Append new values in
- read all current values
- delete a chosen entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
   array = []
   while True:
    print("1. Append new values")
    print("2. Read all current values")
    print("3. Delete a chosen entry")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        row = int(input("Enter the row number: "))
        column = int(input("Enter the column number: "))
        value = input("Enter the value: ")
        while len(array) <= row:
            array.append([])
        while len(array[row]) <= column:
            array[row].append(None)
        array[row][column] = value
    elif choice == "2":
        for row in array:
            print(row)
    elif choice == "3":
        row = int(input("Enter the row number: "))
        column = int(input("Enter the column number: "))
        if row < len(array) and column < len(array[row]):
            array[row][column] = None
        else:
            print("Invalid row or column number.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
