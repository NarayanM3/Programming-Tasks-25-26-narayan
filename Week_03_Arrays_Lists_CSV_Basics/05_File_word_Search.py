"""
TASK: 05 File Word Search

# Skills: File reading, loops, Data mining
Ask user for a filename and a search term. https://sherlock-holm.es/ascii/ is a site that has the entire collection of Sherlock Holmes
Load the file and count how many lines contain the search term

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import urllib.request

import urllib.request
import ssl

import urllib.request
import ssl

def main():
    search_term = input("Enter the search term: ")

    url = "https://sherlock-holm.es/stories/plain-text/cano.txt"

    context = ssl._create_unverified_context()

    count = 0

    with urllib.request.urlopen(url, context=context) as file:
        for line in file:
            line = line.decode("utf-8")

            if search_term.lower() in line.lower():
                count += 1

    print("Number of lines containing the search term:", count)


if __name__ == "__main__":
    main()