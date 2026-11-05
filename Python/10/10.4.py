a = int(input("Enter the number: "))
n = int(input("Enter the number: "))

def power_iter(a, n):
    """Return a raised to the power n using iterative multiplication."""
    result = 1
    for i in range(n):
        result *= a
    return result

def power_rec(a, n):
    """Return a raised to the power n using recursive exponentiation."""
    if n == 0:
        return 1
    result = (power_rec(a, n//2))
    if n % 2 == 0:
        result *= result
    else:
        result *= result*a
    return result

print(f"iter {power_iter(a,n)}, rec {power_rec(a,n)}")

assert power_iter(0, 1) == power_rec(0, 1)
assert power_iter(5, 2) == power_rec(5, 2)
assert power_iter(15, 3) == power_rec(15, 3)