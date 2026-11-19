a = int(input("Enter the number: "))
if a > 0:
    b = "positive"
elif a < 0:
    b = "negative"
else:
    b = "zero"
print(f"{a} is {b}")

x = 7
assert (x > 0)
x = -7
assert (x < 0)
x = 0
assert (x == 0)
x = -1
assert (x < 0)