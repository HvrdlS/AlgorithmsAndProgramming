a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

def gcd_iter(a,b):
    """Return the greatest common divisor of a and b using iteration."""
    while b != 0:
        a, b = b, a%b
    return a 

def gcd_rec(a,b):
    """Return the greatest common divisor of a and b using recursion."""
    if b == 0:
        return a
    return gcd_rec(b, a%b)
print(f"iter {gcd_iter(a,b)}, rec {gcd_rec(a,b)}")

assert gcd_iter(18,6) == gcd_rec(18,6)
assert gcd_iter(1,1) == gcd_rec(1,1)
assert gcd_iter(24,4) == gcd_rec(24,4)