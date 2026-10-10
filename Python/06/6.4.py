n = int(input("Enter the number: "))
s = 0
while n > 0:
    digit = n % 10
    s = s * 10 + digit
    n //= 10
print(f"{s}") 