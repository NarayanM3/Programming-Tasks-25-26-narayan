"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add itemds to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    shopping_list = []
    while True:
        item = input("Enter an item for the shopping list (or type 'Q' to quit): ")
        if item.lower() == 'q':
            break

        shopping_list.append(item)

    print("Shopping list: ", shopping_list)

    for i in range(len(shopping_list)):
        print(i + 1, shopping_list[i])

    edit = input("Do you want to edit an item? (y/n): ")

    if edit.lower() == 'y':
        item_number = int(input("Enter the number of the item to edit: "))
        new_item = input("Enter the new item: ")
        shopping_list[item_number - 1] = new_item

    print("Updated shopping list: ", shopping_list)

    for i in range(len(shopping_list)):
        print(i + 1, shopping_list[i])



if __name__ == "__main__":
    main()
