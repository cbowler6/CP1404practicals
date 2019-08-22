"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    grade = calc_grade(score)
    print(grade)


def calc_grade(score):
    if score < 0 or score > 100:
        grade = "invalid score"
    elif score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "bad"
    return grade


main()
