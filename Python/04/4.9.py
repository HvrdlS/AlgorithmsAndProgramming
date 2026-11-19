a = int(input("Enter the 2-digit number: "))
reverse = a % 10 * 10 + a // 10
digit_sum = a + reverse
print(f"{reverse}, sum = {digit_sum}")