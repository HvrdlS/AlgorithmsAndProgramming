n = int(input("Enter the number: "))
s = 0
k = []
div = 1
while div <= n:
    if n % div == 0: 
        s += 1
        k.append(div)
    div += 1
print(f"{k} ({s} divisors)")