def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
   score = int(input("Enter your score (0-100): "))
   grade = get_grade(score)
   print("Your grade is: ", grade)


if __name__ == "__main__":
    main()
