a, b, c = map(int, input("Enter three numbers: ").split())
m = a
if b > m: 
    m = b
if c > m:
    m = c
print(f"{m}")