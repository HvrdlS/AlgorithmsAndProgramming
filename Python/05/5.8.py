import math
a, b, c = map(int,input("Enter three numbers: ").split())
if a == 0:
    result = f"linear: x = {-c / b}"
else:
    D = b**2 - (4 * a * c)
    if D < 0:
        result = "not defined"
    elif D == 0:
        result = f"x = {-b / (2 * a)}"
    elif D > 0:
        result = f"x1 = {(-b + math.sqrt(D)) / (2 * a)}, x2 = {(-b - math.sqrt(D)) / (2 * a)}"
print(f"{result}")