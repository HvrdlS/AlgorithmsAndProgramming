n = int(input("Enter the number: "))

def binary_rec(n):
    """Return the binary representation of n using recursion."""
    if n < 2:
        return str(n)
    return binary_rec(n // 2) + str(n % 2)


def binary_iter(n):
    """Return the binary representation of n using iteration."""
    if n == 0:
        return "0"

    result = ""
    while n > 0:
        result = str(n % 2) + result
        n //= 2

    return result

print(f"iter {binary_iter(n)}, rec {binary_rec(n)}")

assert binary_rec(0) == "0"
assert binary_rec(10) == "1010"
assert binary_rec(255) == "11111111"
assert binary_iter(0) == "0"
assert binary_iter(10) == "1010"
assert binary_iter(255) == "11111111"