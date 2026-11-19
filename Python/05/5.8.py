import math
a, b, c = map(int,input("Enter three numbers: ").split())
if a == 0:
    if b == 0:
        if c == 0:
            result = "infinite solutions"
        else:
            result = "no solution"
    else:
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
a, b, c = 1, -3, 2
assert b**2 - 4*a*c > 0
a, b, c = 1, 2, 1
assert b**2 - 4*a*c == 0
a, b, c = 1, 0, 1
assert b**2 - 4*a*c < 0
a, b, c = 0, 0, 0
assert a == 0 and b == 0 and c == 0