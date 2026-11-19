a = int(input("Enter the number: "))
firstnum = a // 100
secondnum = (a // 10) % 10
thirdnum = a % 10
digit_sum = firstnum + secondnum + thirdnum
print(f"{firstnum}:{secondnum}:{thirdnum}, Sum = {digit_sum}")