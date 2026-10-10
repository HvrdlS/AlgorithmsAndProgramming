n = int(input("Enter the number: "))
a, b = 0, 1
s = 0
for i in range(n):
    print(f"{a:1d}")
    s += a
    a, b = b, a + b
print(f"Sum: {s}")