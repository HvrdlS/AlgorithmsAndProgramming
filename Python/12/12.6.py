"""Data types: dictionary, key, and score value.
Dictionary key-value lookup and maximum/minimum key selection are used;
scanning n entries takes O(n) time, with average O(1) dictionary access.
"""

students = dict([("Shevchenko", 92), ("Koval", 74), ("Bondar", 92), ("Tkach", 58)])
best = max(students,key=students.get)
worst = min(students,key=students.get)
print(f"Best: {best} {students[best]}, worst: {worst} {students[worst]}")