import numpy as np

# ---- ARRAYS (1) ----
marks = np.array([
    [85, 78, 92, 88],
    [72, 69, 75, 80],
    [90, 95, 89, 94],
    [60, 65, 70, 68],
    [88, 84, 91, 87]
])

# ---- SHAPE (1) ----
n_students, n_subjects = marks.shape
print(f"Shape: {marks.shape} -> {n_students} students, {n_subjects} subjects\n")

# ---- INDEXING (1): get a single student's row ----
print("First student's marks:", marks[0])

# ---- SLICING (1): get all marks for the first subject (all rows, column 0) ----
print("All marks in Subject 1:", marks[:, 0], "\n")

# ---- AXIS + AGGREGATION (1): per-student stats -> axis=1 (across each row) ----
student_avg = marks.mean(axis=1)
student_high = marks.max(axis=1)
student_low = marks.min(axis=1)
student_std = marks.std(axis=1)

# ---- AXIS + AGGREGATION (2): per-subject stats -> axis=0 (across each column) ----
subject_avg = marks.mean(axis=0)
subject_high = marks.max(axis=0)
subject_low = marks.min(axis=0)

# Class average = aggregation with no axis (whole matrix)
class_avg = marks.mean()

print("Student averages:", student_avg)
print("Student highest:", student_high)
print("Student lowest:", student_low)
print("Student std dev:", student_std, "\n")

print("Subject averages:", subject_avg)
print("Subject highest:", subject_high)
print("Subject lowest:", subject_low, "\n")

print(f"Class average: {class_avg:.2f}")

# ---- BROADCASTING (1): compare array of averages to a single scalar ----
above_avg_mask = student_avg > class_avg
print("Above class average?:", above_avg_mask)

# ---- BROADCASTING (2): subtract scalar class average from every mark at once ----
diff_from_class_avg = marks - class_avg

# ---- VECTORIZATION (1): pass/fail for every student, no loop ----
pass_fail = np.where(student_avg >= 40, "Pass", "Fail")
print("Pass/Fail:", pass_fail)

# ---- VECTORIZATION (2): find the top student without a loop ----
top_student_index = np.argmax(student_avg)
print(f"\nTop student: Student {top_student_index + 1} "
      f"(avg = {student_avg[top_student_index]:.2f})")

print(f"Students above class average: {above_avg_mask.sum()}")