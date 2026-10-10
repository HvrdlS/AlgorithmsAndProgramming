import math 
a, b = map(int, input("Enter two numbers: ").split())
GCD = math.gcd(a, b)
LCM = (a * b) // GCD
print(f"GCD = {GCD}, LCM = {LCM}")