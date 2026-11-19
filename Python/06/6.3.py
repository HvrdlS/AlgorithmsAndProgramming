n = int(input("Enter the number: "))
m = -float("inf")
l = float("inf")
while n > 0:
    digit = n % 10
    n //= 10
    if digit > m: m = digit
    if digit < l: l = digit
print(f"max = {m}, min = {l}")