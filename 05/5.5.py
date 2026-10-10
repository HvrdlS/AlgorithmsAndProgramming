a, b, c = map(int, input("Enter three numbers: ").split())
if a + b < c or a + c < b or b + c < a:
    print(f"not a triangle")
elif a != b and b != c and a != c:
    print(f"scalene")
elif a == b or b == c or a == c:
    if a != b or a!= c:
        print(f"isosceles")
    else: print(f"equilateral")