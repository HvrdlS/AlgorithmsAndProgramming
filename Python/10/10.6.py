from functools import lru_cache
n = int(input("Enter the number: "))

def fib_iter(n):
    """Return the nth Fibonacci number using iteration."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
    
def fib_rec(n):
    """Return the nth Fibonacci number using naive recursion."""
    if n <= 1:
        return n
    return fib_rec(n-1)+fib_rec(n-2)


@lru_cache(maxsize=None)
def fib_rec_memo(n):
    """Return the nth Fibonacci number using memoized recursion."""
    if n <= 1:
        return n
    return fib_rec(n-1)+fib_rec(n-2)

print(f"iter {fib_iter(n)}, rec(memo) {fib_rec_memo(n)}")

assert fib_rec_memo(5) == fib_iter(5)
assert fib_rec_memo(15) == fib_iter(15)
assert fib_rec_memo(35) == fib_iter(35)
