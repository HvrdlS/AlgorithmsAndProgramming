a = list(map(int, input("Input the numbers: ").split()))
result = []
for x in a:
    if x not in result:
        result.append(x)
print(result)