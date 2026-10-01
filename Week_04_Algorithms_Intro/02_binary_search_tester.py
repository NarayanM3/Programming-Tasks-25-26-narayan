"""
TASK: 02 Binary Search Tester

# Binary Search Tester
Generate a sorted list. Implement:
- iterative binary search
- recursive binary search
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


import random
import time


def binary_search_iterative(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(nums, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, high)
    else:
        return binary_search_recursive(nums, target, low, mid - 1)



def main():
    amount = int(input("Enter the number of numbers you want to generate: "))
    nums = random.sample(range(1, 100000), amount)
    nums.sort()
    print("Sorted list: ", nums)
    target = int(input("Enter the target number to search for: "))

    start_time = time.time()
    result_iterative = binary_search_iterative(nums, target)
    end_time = time.time()
    print("Iterative result: ", result_iterative)
    print("Iterative time: ", end_time - start_time)

    start_time = time.time()
    result_recursive = binary_search_recursive(nums, target, 0, len(nums) - 1)
    end_time = time.time()
    print("Recursive result: ", result_recursive)
    print("Recursive time: ", end_time - start_time)


if __name__ == "__main__":
    main()
