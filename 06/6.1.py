n = int(input("Enter the number: "))
s = 0
p = 1
while n > 0:
    digit = n % 10
    s += digit
    p *= digit
    n //= 10
print(f"sum = {s}, product = {p}")