n = int(input("Enter the number: "))
s = 0
for x in range(2, n + 1):
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False

    if prime:
        print(f"{x}")
        s += 1
print(f"{s} numbers")