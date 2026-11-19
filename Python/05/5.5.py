a, b, c = map(int, input("Enter three numbers: ").split())
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print(f"not a triangle")
elif a != b and b != c and a != c:
    print(f"scalene")
elif a == b or b == c or a == c:
    if a != b or a!= c:
        print(f"isosceles")
    else: print(f"equilateral")

a, b, c = 3, 4, 5
assert a + b > c and a + c > b and b + c > a
a, b, c = 3, 3, 5
assert a == b or b == c or a == c
a, b, c = 3, 3, 3
assert a == b == c
a, b, c = 1, 2, 3
assert not (a + b > c and a + c > b and b + c > a)