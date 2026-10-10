a = int(input("Enter the 5-digit number:" ))
firstnum = a // 10000
secondnum = a // 1000 % 10
thirdnum = a // 100 % 10 
fourthnum = a // 10 % 10
fifthnum = a % 10
sum = firstnum + secondnum + thirdnum + fourthnum + fifthnum
product = firstnum * secondnum * thirdnum * fourthnum * fifthnum
print(f"sum = {sum}, product = {product}")