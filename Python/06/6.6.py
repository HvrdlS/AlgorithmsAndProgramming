n = int(input("Enter the number: "))
if n < 2: status = "Neither prime nor composite"
else:
    status = "Prime"
    d = 2
    while d * d <= n:
        if n % d == 0:
            status = "Composite"
            break       
        d += 1
print(f"{status}")