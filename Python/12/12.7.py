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