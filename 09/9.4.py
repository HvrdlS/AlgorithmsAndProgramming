m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

main_sum = sum(a[i][i] for i in range(n))
secondary_sum = sum(a[i][n-1-i] for i in range(n))
print(f"main = {main_sum}, secondary = {secondary_sum}")