m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

positive = 0
negative = 0
zeros = 0
for i in range(m):
    for j in range(n):
        if a[i][j] > 0:
            positive += 1
        elif a[i][j] < 0:
            negative += 1
        else: zeros += 1
print(f"positive {positive}, negative {negative}, zeros {zeros}")