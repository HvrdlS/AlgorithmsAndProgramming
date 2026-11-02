a = list(map(int, input("Input the numbers: ").split()))
even_sum = 0
odd_sum = 0
for i in range(len(a)):
    if i % 2 == 0:
        even_sum += a[i]
    else:
        odd_sum += a[i]
print(f"even indices {even_sum}, odd indices {odd_sum}")