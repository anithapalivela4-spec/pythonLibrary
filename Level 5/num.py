import numpy as np
names = np.array([
    "Anitha",
    "Binnu",
    "kalyani",
    "Reshma",
    "Anu"
])


marks = np.array([
    [85, 90, 88],
    [70, 75, 80],
    [95, 92, 96],
    [45, 50, 40],
    [80, 85, 82]
])

total = np.sum(marks, axis=1)

print("Total Marks:")
for i in range(len(names)):
    print(names[i], ":", total[i])

average = np.mean(marks, axis=1)

print("\nAverage Marks:")
for i in range(len(names)):
    print(names[i], ":", round(average[i], 2))


highest_index = np.argmax(total)

print("\nHighest Scorer:")
print(names[highest_index], ":", total[highest_index])


lowest_index = np.argmin(total)

print("\nLowest Scorer:")
print(names[lowest_index], ":", total[lowest_index])

subject_average = np.mean(marks, axis=0)

print("\nSubject-wise Average:")

subjects = ["Python", "SQL", "NumPy"]

for i in range(len(subjects)):
    print(subjects[i], ":", round(subject_average[i], 2))




pass_students = np.all(marks >= 40, axis=1)

pass_count = np.sum(pass_students)
fail_count = np.sum(~pass_students)

print("\nPass Count:", pass_count)
print("Fail Count:", fail_count)



print("\nGrades:")

for i in range(len(names)):

    avg = average[i]

    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "F"

    print(names[i], ":", grade)



rank_indexes = np.argsort(total)[::-1]

print("\nRank:")

for rank, index in enumerate(rank_indexes, start=1):
    print(rank, names[index], total[index])



class_average = np.mean(average)

print("\nClass Average:", round(class_average, 2))




print("\nStudents Above Class Average:")

for i in range(len(names)):

    if average[i] > class_average:
        print(names[i], ":", round(average[i], 2))