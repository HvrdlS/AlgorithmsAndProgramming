m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

sum = 0
max, min, pi_max, pj_max, pi_min, pj_min = a[0][0], a[0][0], 0, 0, 0, 0
for i in range(m):
    for j in range(n):
        sum += a[i][j]
        if a[i][j] > max:
            max, pi_max, pj_max = a[i][j], i, j
        if a[i][j] < min:
            min, pi_min, pj_min = a[i][j], i, j
print(f"max {max}, ({pi_max, pj_max}), min {min}, ({pi_min, pj_min}), sum= {sum}")