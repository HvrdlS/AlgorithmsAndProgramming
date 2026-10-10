a = int(input("Enter the number: "))
if a > 0:
    b = "positive"
elif a < 0:
    b = "negative"
else:
    b = "zero"
print(f"{a} is {b}")