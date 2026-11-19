a = int(input("Enter the number: "))
def digit_count_iter(n):
    """Return the number of digits in n using iteration."""
    if n == 0:
        return 1
    k = 0
    n = abs(n)
    while n > 0:
        k += 1
        n = n//10
    return k 

def digit_count_rec(n):
    """Return the number of digits in n using recursion."""
    n = abs(n)
    if n < 10:
        return 1
    return 1 + digit_count_rec(n//10)

print(f"iter {digit_count_iter(a)}, rec {digit_count_rec(a)}")
assert digit_count_rec(55) == 2
assert digit_count_rec(0) == 1
assert digit_count_rec(75655) == 5
assert digit_count_iter(55) == 2
assert digit_count_iter(0) == 1
assert digit_count_iter(75655) == 5

