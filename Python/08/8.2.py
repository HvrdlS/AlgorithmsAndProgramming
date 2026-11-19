a = list(map(int, input("Input the numbers: ").split()))
if not a:
    print("Empty list")
else:
    maximum_value = a[0]
    pos_max = 0
    minimum_value = a[0]
    pos_min = 0
    for i in range(1, len(a)):
        if a[i] > maximum_value:
            maximum_value, pos_max = a[i], i
        if a[i] < minimum_value:
            minimum_value, pos_min = a[i], i
    print(f"max={maximum_value}, (index {pos_max}), min={minimum_value} (index {pos_min})")