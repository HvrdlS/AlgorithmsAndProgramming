number = int(input("Enter a number of kopiykas: "))
hrn = number // 100
kop = number % 100
print(f"{hrn} UAH {kop:02d} kop")