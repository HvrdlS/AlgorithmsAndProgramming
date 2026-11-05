a = list(map(int, input("Input the numbers: ").split()))
positive = 0
negative = 0
zeros = 0
for i in range(len(a)):
    if a[i] > 0:
        positive += 1
    elif a[i] < 0:
        negative += 1
    elif a[i] == 0:
        zeros += 1
print(f"positive {positive}, negative {negative}, zeros {zeros}")