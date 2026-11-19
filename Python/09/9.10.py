m, n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
b = [list(map(int, input().split())) for _ in range(n)]

c = [[sum(a[i][t] * b[t][j] for t in range(n))
      for j in range(k)] for i in range(m)]

for row in c:
    print(" ".join(f"{x:4d}" for x in row))
