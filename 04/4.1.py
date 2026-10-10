a = int(input("Enter the 4-digit number: "))
reverse = (a % 10 * 1000) + (a // 10 % 10 * 100) + (a // 100 % 10 * 10) + (a // 1000)
print(f"{reverse}")