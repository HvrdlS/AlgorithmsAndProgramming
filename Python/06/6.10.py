n = int(input("Enter the number: "))
s = 0
k = 0
for i in range(1, n):
    if n % i == 0:
        s += i
        
if n == s: 
    print(f"perfect")
else: print(f"not perfect")