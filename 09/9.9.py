m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

b = [[a[n - 1 - j][i] for j in range(n)] for i in range(n)]
for row in b:
    print(" ".join(f"{x:4d}" for x in row))