A = [1,3,5,7,9,11]
target = int(input("Enter the target: "))


def binary_search_iter(a, target):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
    
def bsearch_rec(a, target, lo=0, hi=None):
    if hi is None:
        hi = len(a) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if a[mid] == target:
        return mid
    if a[mid] < target:
        return bsearch_rec(a, target, mid + 1, hi)
    return bsearch_rec(a, target, lo, mid - 1)
    
print(f"target {target}, iter {binary_search_iter(A, target)}, rec {bsearch_rec(A, target)}")