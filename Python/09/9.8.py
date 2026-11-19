m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

a.sort(key=sum)
print(a)