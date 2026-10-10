a = int(input("Enter the 3-digit number: "))
reverse = a % 10 * 100 + a // 10 % 10 * 10 + a // 100
print(f"{reverse}")