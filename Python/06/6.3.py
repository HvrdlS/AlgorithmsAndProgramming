n = int(input("Enter the number: "))
s = 0
m = -float("inf")
l = float("inf")
while n > 0:
    digit = n % 10
    s += digit
    n //= 10
    if digit > m: m = digit
    if digit < l: l = digit
print(f"max = {m}, min = {l}")