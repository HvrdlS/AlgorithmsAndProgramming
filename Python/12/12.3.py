a = list(map(int,input("Enter numbers: ").split()))
unique_set = set(a)
unique_order = []
for num in a:
    if num not in unique_order:
        unique_order.append(num)

print(f"set: {unique_set}, order: {unique_order}")