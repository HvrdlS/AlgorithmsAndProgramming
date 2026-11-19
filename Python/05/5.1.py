a, b, c = map(int, input("Enter three numbers: ").split())
m = a
if b > m: 
    m = b
if c > m:
    m = c
print(f"{m}")

x, y, z = 1, 2, 3
assert max(x, y, z) == 3
x, y, z = 10, 5, 7
assert max(x, y, z) == 10
x, y, z = -3, -1, -2
assert max(x, y, z) == -1
x, y, z = 4, 4, 4
assert max(x, y, z) == 4