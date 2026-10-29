a = list(map(int, input("Input the numbers: ").split()))
max = a[0]
pos_max = 0
min = a[0]
pos_min = 0
for i in range(1, len(a)):
    if a[i] > max:
        max, pos_max = a[i], i
    if a[i] < min:
            min, pos_min = a[i], i
print(f"max={max}, (index {pos_max}), min={min} (index {pos_min})")