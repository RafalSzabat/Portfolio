
student_grade_tracker = {}


while True:
    name = input("Enter a student name: ")
    grade = int(input(f'Enter {name} grade: '))
    student_grade_tracker[name] = grade

    for name, grade in student_grade_tracker.items():

        print(f"{name} → {grade}")

    cont = input("Add another? (y/n): ").lower()

    if cont != 'y':

        average_grades = sum(student_grade_tracker.values()) / len(student_grade_tracker)
        print(f'Grade summary:')
        for key, value in student_grade_tracker.items():
            print("{}: {}".format(key, value))
        print("Average:", round(average_grades, 2))
        break