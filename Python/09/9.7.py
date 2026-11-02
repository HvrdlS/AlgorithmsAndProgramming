m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

i, k = map(int, input("Which rows to swap: ").split())
a[i], a[k] = a[k], a[i]

j, k = map(int, input("Which columns to swap: ").split())
for i in range(m):
    a[i][j], a[i][k] = a[i][k], a[i][j]
for row in a:
    print(" ".join(f"{x:4d}" for x in row))