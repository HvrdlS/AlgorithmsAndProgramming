m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

above = sum(a[i][j] for i in range(n) for j in range(n) if i < j)
below = sum(a[i][j] for i in range(n) for j in range(n) if i > j)

print(f"above {above}, below {below}")