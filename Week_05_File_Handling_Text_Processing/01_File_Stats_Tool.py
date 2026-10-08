"""
TASK: 01 File Stats Tool

# Read a .txt file and compute:
Task:
- Number of lines
- Number of words
- Number of characters
- Most frequent word

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

from fileinput import filename


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def count_lines(text):
    return len(text.splitlines())

def count_words(text):
    return len(text.split())

def count_characters(text):
    return len(text)

def most_frequent_word(text):
    words = text.lower().split()
    word_count = {}
    for i in range(len(words)):
       word = words[i].strip('.,!?";:()[]{}')
       word_count[word] = word_count.get(word, 0) + 1
    return max(word_count, key=word_count.get)


def main():
    filename = "requirements.txt"
    text = read_file(filename)
    print("Number of lines: ", count_lines(text))
    print("Number of words: ", count_words(text))
    print("Number of characters: ", count_characters(text))
    print("Most frequent word: ", most_frequent_word(text))


if __name__ == "__main__":
    main()
