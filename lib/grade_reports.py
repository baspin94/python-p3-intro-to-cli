#!/usr/bin/env python3

def create_grade_report(student_grades):
    # open a file named grade_report in write ('w') mode, create if doesn't exist
    with open('reports/grade_report.txt', 'w') as gr:
        for grade in student_grades:
            # use the write method to write the specified text to the file.
            gr.write(grade + '\n') # grade and then insert new line.

if __name__ == '__main__':
    # Executing this way will only let you input one grade.
        # student_grades = input("Student name, grade: ")
        # create_grade_report(student_grades)
    # Executing this way will loop until you don't enter a value:
    student_grades = []
    grade = input("Student name, grade: ")
    while grade:
        student_grades.append(grade)
        # end when no grade is entered
        grade = input("Student name, grade: ")
    
    create_grade_report(student_grades)
