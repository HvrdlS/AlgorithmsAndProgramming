a = abs(int(input("Enter the number: ")))
def digit_sum_iter(n):
    """Return the sum of the digits in n using iteration."""
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum

def digit_sum_rec(n):
    """Return the sum of the digits in n using recursion."""
    if n == 0:
        return 0
    return (n % 10) + digit_sum_rec(n//10)

print(f"iter {digit_sum_iter(a)}, rec {digit_sum_iter(a)}")
assert digit_sum_rec(0) == 0
assert digit_sum_rec(5) == 5
assert digit_sum_rec(1234) == 10
assert digit_sum_iter(0) == 0
assert digit_sum_iter(5) == 5
assert digit_sum_iter(1234) == 10