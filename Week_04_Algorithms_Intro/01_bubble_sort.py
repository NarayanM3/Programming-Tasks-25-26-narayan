"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def bubble_sort(nums):
    swaps = 0
    for i in range(len(nums)):
        for j in range(0, len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swaps += 1
    return nums, swaps


def main():
    nums = []
    amount = int(input("Enter the number of numbers you want to sort: "))
    for i in range(amount):
        num = int(input("Enter number " + str(i + 1) + ": "))
        nums.append(num)

    print("Original list: ", nums)
    swaps = bubble_sort(nums)
    print("Sorted list: ", nums)
    print("Number of swaps: ", swaps)

if __name__ == "__main__":
    main()
