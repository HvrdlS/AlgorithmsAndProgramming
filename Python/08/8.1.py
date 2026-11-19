a = list(map(int, input("Input the numbers: ").split()))
total = sum(a)
n = len(a)
if n == 0:
    mean = 0
    product = 0
else:
    mean = total / n
    product = 1
    for i in range(n):
        product *= a[i]
print(f"sum {total}, product {product}, n {n}, mean {mean}")