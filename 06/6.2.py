n = int(input("Enter the number: "))
s = 0
k = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0: k += 1
    s += 1
    n //= 10
print(f"digits = {s}, even = {k}")