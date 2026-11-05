import math
a, b = map(float, input("Enter two legs of a right triangle: ").split())
hypotenuse = math.hypot(a, b)
perimeter = a + b + hypotenuse
area = (a * b) / 2
print(f"c = {hypotenuse:.2f}, P = {perimeter:.2f}, S = {area:.2f}")