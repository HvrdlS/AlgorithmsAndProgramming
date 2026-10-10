a = int(input("Enter a 6-digit number: "))
d = a // 10000
m = a // 100 % 100
y = a % 100
print(f"{d:02d}.{m:02d}.20{y:01d}")