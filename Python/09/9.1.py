m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

total = 0
maximum, minimum, pi_max, pj_max, pi_min, pj_min = a[0][0], a[0][0], 0, 0, 0, 0
for i in range(m):
    for j in range(n):
        total += a[i][j]
        if a[i][j] > maximum:
            maximum, pi_max, pj_max = a[i][j], i, j
        if a[i][j] < minimum:
            minimum, pi_min, pj_min = a[i][j], i, j
print(f"max {maximum}, ({pi_max, pj_max}), min {minimum}, ({pi_min, pj_min}), sum= {total}")