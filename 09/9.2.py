m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

m = len(a)
n = len(a[0])
print("rows: ", end=" ")
for i in range(m):
    rows_sum = 0
    for j in range(n):
        rows_sum += a[i][j]
    print(rows_sum, end=" ")
        
print("\ncolumns: ", end=" ")
for j in range(n):
    columns_sum = 0
    for i in range(m):
        columns_sum += a[i][j]
    print(columns_sum, end=" ")