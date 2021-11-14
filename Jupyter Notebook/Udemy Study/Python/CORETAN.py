grades_count = int(input())
grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

final_grades = []
for i in grades:
    if i >= 38:
        if 5-(i % 5) < 3:
            final_grades.append(i+5-(i % 5))
        else:
            final_grades.append(i)
    else:
        final_grades.append(i)
print(final_grades)
