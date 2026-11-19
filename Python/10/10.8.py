a = str(input("Enter the word: "))

def is_palindrome_iter(a):
    """Return True if a is a palindrome using an iterative check."""
    for i in range(len(a)//2):
       if a[i] != a[len(a)-1-i]:
           return False
    return True

def is_palindrome_rec(a):
    """Return True if a is a palindrome using recursive checks."""
    if len(a) <= 1:
        return True
        
    if a[0] != a[-1]:
        return False
    return is_palindrome_rec(a[1:-1])

print(f"iter {is_palindrome_iter(a)}, rec {is_palindrome_rec(a)}")

assert is_palindrome_rec("radar") is True
assert is_palindrome_rec("platform") is False
assert is_palindrome_rec("python") is False
assert is_palindrome_iter("radar") is True
assert is_palindrome_iter("platform") is False
assert is_palindrome_iter("python") is False