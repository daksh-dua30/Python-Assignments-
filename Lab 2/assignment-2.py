# Name: Daksh
# Date: 27 October, 2025
# Title: GradeBook Analyzer

def manual_input():
    list = {}
    num = int(input("How many students to enter: "))
    for i in range(num):
        print(f"\n--- Enter details for Student {i+1} ---")
        name = input("Enter the name: ")
        marks = float(input("Enter marks: "))
        list[name] = marks
    return list


def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)


def calculate_median(marks_dict):
    marks = sorted(marks_dict.values())
    mid = len(marks) // 2
    n = len(marks)
    if n % 2 == 0:
        return (marks[mid] + marks[mid - 1]) / 2
    else:
        return marks[mid]


def find_max(marks_dict):
    return max(marks_dict.values())


def find_min(marks_dict):
    return min(marks_dict.values())


def grade_section(marks_dict):
    grade = {}
    for name, marks in marks_dict.items():
        if marks >= 90:
            grade[name] = 'A'
        elif marks >= 80:
            grade[name] = "B"
        elif marks >= 70:
            grade[name] = "C"
        elif marks >= 60:
            grade[name] = "D"
        else:
            grade[name] = "F"
    return grade


def grade_distribution(grade_dict):
    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grade_dict.values():
        distribution[grade] += 1
    return distribution


# ---------- MAIN PROGRAM ----------

d = manual_input()
print("\n===================")
print("STUDENT MARKS DATA")
print("=====================")
for name, marks in d.items():
    print(f"{name:<15} : {marks}")

avg = calculate_average(d)
med = calculate_median(d)
maximum_marks = find_max(d)
minimum_marks = find_min(d)

grades = grade_section(d)
grade_dis = grade_distribution(grades)

print("\n====================")
print(" STATISTICS")
print("======================")
print(f"Average Marks       : {avg:.2f}")
print(f"Median Marks        : {med}")
print(f"Highest Marks       : {maximum_marks}")
print(f"Lowest Marks        : {minimum_marks}")

print("\n====================")
print(" GRADES")
print("======================")
for name, grade in grades.items():
    print(f"{name:<15} : Grade {grade}")

print("\n====================")
print(" GRADE DISTRIBUTION")
print("======================")
for grade, count in grade_dis.items():
    print(f"Grade {grade} : {count} student(s)")

print("\n Program Execution Completed Successfully!")
