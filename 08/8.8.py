a = list(map(int, input("Input the numbers: ").split()))
k = int(input("Input k: ")) % len(a)
a = a[k:] + a[:k]
print(a)