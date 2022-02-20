from random import randint

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {name: randint(1, 100) for name in names}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
