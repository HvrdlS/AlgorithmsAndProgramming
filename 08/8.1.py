a = list(map(int, input("Input the numbers: ").split()))
sum = sum(a)
n = len(a)
mean = sum/n
for i in range(n):
    if i == 0:
        product = a[i]
    else:
        product *= a[i]
print(f"sum {sum}, product {product}, n {n}, mean {mean}")