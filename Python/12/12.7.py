"""Data types: list of tuples and dictionary of lists.
Tuples keep each surname-score pair together; the dictionary maps each
grade to a list for grouped storage. Processing n pairs takes O(n) average
time because dictionary operations are average O(1).
"""

students = [("Shevchenko", 92), ("Koval", 74), ("Bondar", 92), ("Tkach", 58)]
groups = {}

for surname, score in students:
    if score >= 90:
        grade = "A"
    elif score >= 74:
        grade = "C"
    else:
        grade = "FX"

    groups.setdefault(grade, []).append(surname)

print(groups)