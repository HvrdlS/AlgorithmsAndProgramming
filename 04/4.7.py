a = int(input("Enter a four-digit number: "))
new_num = a % 1000 * 10 + a // 1000
print(f"{new_num}")