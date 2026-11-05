a = list(map(int, input("Enter the number: ").split()))
def list_sum_rec(a):
    """Return the sum of all values in a list using recursion."""
    if len(a) == 0:
        return 0
    return a[0] + list_sum_rec(a[1:])


def list_sum_iter(a):
    """Return the sum of all values in a list using iteration."""
    total = 0
    for i in a:
        total += i
    return total

print(f"iter {list_sum_iter(a)}, rec {list_sum_rec(a)}")

assert list_sum_rec([]) == list_sum_iter([])
assert list_sum_rec([5]) == list_sum_iter([5])
assert list_sum_rec([1, 2, 3, 4]) == list_sum_iter([1, 2, 3, 4])