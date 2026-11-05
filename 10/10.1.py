a = abs(int(input("Enter the number: ")))
def factorial_iter(n):
    """Return the factorial of n using an iterative loop."""
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_rec(n):
    """Return the factorial of n using recursive calls."""
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)

print(f"iter - {factorial_iter(a)}, rec {factorial_rec(a)}")
assert factorial_iter(0) == 1
assert factorial_iter(1) == 1
assert factorial_iter(5) == 120

assert factorial_rec(0) == 1
assert factorial_rec(1) == 1
assert factorial_rec(5) == 120