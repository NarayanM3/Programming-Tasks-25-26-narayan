"""
TASK: 05 String Parser

# String Parser
Write a parser that:
- Accepts a sentence from the user.
- Splits it into words manually (not using split()).
- Outputs number of words + list of words.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


def parsed_sentence(sentence):
    words = []
    current_word = ""
    for i in sentence:
        if i != " ":
            current_word += i
        else:
            if current_word != "":
                words.append(current_word)
                current_word = ""
    if current_word != "":
        words.append(current_word)
        return words


def main():
    sentence = input("Enter a sentence: ")
    words = parsed_sentence(sentence)
    print("Words - ", words)
    print("number of words - ", len(words))


if __name__ == "__main__":
    main()
