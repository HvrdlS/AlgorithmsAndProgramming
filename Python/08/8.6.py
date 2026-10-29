a = list(map(int, input("Input the numbers: ").split()))
original_id = id(a)
for i in range(len(a)//2):
    a[i], a[-1-i] = a[-1-i], a[i]
print(a, "Same list object:", id(a) == original_id)