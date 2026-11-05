a = int(input("Enter the number: "))
def digit_count_iter(n):
    """Return the number of digits in n using iteration."""
    k = 0
    while n > 0:
        k += 1
        n = n//10
    return k 

def digit_count_rec(n):
    """Return the number of digits in n using recursion."""
    k = 0 
    if n == 0:
        return 0 
    k = 1 + digit_count_rec(n//10)
    return k 

print(f"iter {digit_count_iter(a)}, rec {digit_count_rec(a)}")
assert digit_count_rec(55)==digit_count_iter(55)
assert digit_count_rec(0)==digit_count_iter(0)
assert digit_count_rec(75655)==digit_count_iter(75655)

