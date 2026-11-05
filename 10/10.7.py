n = int(input("Enter the number: "))

def reverse_number_iter(n):
    """Return the reverse of n using iteration."""
    num = 0 
    while n != 0:
        num = num*10 + n%10
        n //= 10
    return num

def reverse_number_rec(n):
    """Return the reverse of n using recursive digit processing."""
    if n == 0:
        return 0
    return (n%10) * (10**(len(str(n))-1)) + reverse_number_rec(n//10)
print(f"iter {reverse_number_iter(n)}, rec {reverse_number_rec(n)}")

assert reverse_number_iter(0) == reverse_number_rec(0)
assert reverse_number_iter(895) == reverse_number_rec(895)
assert reverse_number_iter(100) == reverse_number_rec(100)
