import math
a, b, c, d = map(int, input("Enter two point coordinates (x1 y1 x2 y2):").split())
distance = math.hypot(c-a, d-b)
print(f"d= {distance:.2f}")