"""
TASK: 03 Insertion Sort

# Insertion Sort Tester
Generate an unsorted list (maybe use RNG). Implement:
- Insertion sort without using inbuild sorts
- Count number of comparions
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


import random
import time

def insertion_sort(nums):
    comparisons = 0
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if nums[j] > current:
                nums[j + 1] = nums[j]
                j -= 1
            else:
                break
        nums[j + 1] = current
    return comparisons

def main():
    amount = int(input("Enter the number of numbers you want to generate: "))
    numbers = []
    for i in range(amount):
        numbers.append(random.randint(1, 1000))
    print("Unsorted list: ", numbers)
    start_time = time.perf_counter()
    comparisons = insertion_sort(numbers)
    end_time = time.perf_counter()
    print("sorted list: ", numbers)
    print("Number of comparisons: ", comparisons)
    print("Time taken: ", end_time - start_time)


if __name__ == "__main__":
    main()
