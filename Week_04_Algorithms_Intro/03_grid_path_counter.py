"""
TASK: 03 Grid Path Counter

# Grid Path Counter - https://bk2coady.medium.com/daily-coding-problem-62-bfe0e398247b
Given an NxM grid:
- Count paths using recursion
- Count paths using iteration
Movement allowed: RIGHT or DOWN only.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


def recursive_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return recursive_paths(rows - 1, columns) + recursive_paths(rows, columns - 1)

def iterative_paths(rows, columns):
    paths = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        paths[i][0] = 1
    for i in range(columns):
        paths[0][i] = 1
    for i in range(1, rows):
        for j in range(1, columns):
            paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
    return paths[rows - 1][columns - 1]


def main():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    print("Recursive paths:", recursive_paths(rows, columns))
    print("Iterative paths:", iterative_paths(rows, columns))

if __name__ == "__main__":
    main()
