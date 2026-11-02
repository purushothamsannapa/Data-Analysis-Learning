import numpy as np
from pathlib import Path

data_path=Path("data/students.csv")

students= np.genfromtxt(
    data_path,
    delimiter=",",
    skip_header=1,
    usecols=0,
    dtype=str
)

marks=np.genfromtxt(
    data_path,
    delimiter=",",
    skip_header=1,
    usecols=(1,2,3,4),
    dtype=int
)

subject=np.genfromtxt(
    data_path,
    delimiter=",",
    max_rows=1,
    dtype=str
)

subjects_name=subject[1:]

print(students)
print(marks)
print(subject[1:])

print("\ndimensions of marks array: ", marks.ndim)
print("\ndataset shape: ",marks.shape)
print("\ntotal number of students: ",len(students))
print("\ntotal number of subjects:", marks.shape[1])
print("Student data type:", students.dtype)
print("Marks data type:", marks.dtype)

total_marks =np.sum(marks,axis=1)
print("\ntotal marks of each student: ", total_marks)

average_marks = np.mean(marks, axis=1)
print("\naverage marks of each student: ", average_marks)

print("\nStudent data with total marks:")
for student,total in zip(students,total_marks):
    print(f"{student} - {total}")

print("\nStudent data with total and average marks:")
for student, total_mark, average_mark in zip(students,total_marks, average_marks):
    print(f"{student}  Total: {total_mark}  Average: {average_mark:.2f}")

print("\nCLASS TOPPER")
print("----------------")
topper_index= np.argmax(total_marks)

print(f"Student: {students[topper_index]}")
print(f"Average: {average_marks[topper_index]:.2f}")

print("\nPASS STUDENTS")
print("----------------")
pass_student=average_marks>=50
for student,average_mark, pass_studen in zip(students, average_marks, pass_student):
    if pass_studen:
        print(f"{student} - {average_mark:.2f}")

print("\nFAIL STUDENTS")
print("---------------- ")
for student,average_mark, pass_studen in zip(students, average_marks, pass_student):
    if ~pass_studen:
        print(f"{student} - {average_mark:.2f}")

print("\nSubject-wise analysis")
print("-----------------")
average_subject=np.mean(marks,axis=0)
for subject_names, average_subjects in zip(subjects_name, average_subject):
    print(f"{subject_names} - {average_subjects:.2f}")

highest_mark = np.max(marks)
lowest_mark = np.min(marks)
overall_average = np.mean(marks)

print("\nOverall analysis")
print("Highest mark:", highest_mark)
print("Lowest mark:", lowest_mark)
print("Overall average:", overall_average)

print("\nStudent ranking")
print("Rank Name   Average Marks")
ranking = np.argsort(average_marks)[::-1]

for rank,student,average_mark in zip(range(1,len(students)+1), students[ranking], average_marks[ranking]):
    print(f"{rank}:   {student} -   {average_mark:.2f}")

print("STUDENT PERFORMANCE CATEGORIES")
print("-------------------------------")
category=[
    (average_marks >=90),
    (average_marks >=75) & (average_marks <90),
    (average_marks >=60) & (average_marks <75),
    (average_marks >=50) & (average_marks <60)
]

status=["Excellent","Very Good","Good","Average"]
statues_functions=np.select(category,status,default="Fail")

for student, average_mark, status in zip(students, average_marks, statues_functions):
    print(f"{student} - {average_mark:.2f} - {status}")