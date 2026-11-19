students = dict([("Shevchenko", 92), ("Koval", 74), ("Bondar", 92), ("Tkach", 58)])
sorted_students = sorted(students.items(), key=lambda item: (-item[1], item[0]))
print(sorted_students)