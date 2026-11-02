m, n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
b = [list(map(int, input().split())) for _ in range(m)]

if n == k:
    c = [[sum(a[i][t] * b[t][j] for t in range(k))
      for j in range(n)] for i in range(m)]

    for row in c:
        print(" ".join(f"{x:4d}" for x in row))
else: 
   print("Matrixes are not compatible") 
