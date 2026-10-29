a = list(map(int, input("Input the numbers: ").split()))
num = 0
i = 0
while i < len(a):
    if a[i] < 0:
        a.pop(i)
        num += 1
    else: 
        i += 1
print(f"{a}, removed {num}")