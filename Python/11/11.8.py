A = [1,3,5,7,9,11]
target = int(input("Enter the target: "))

def binary_search(a, target):
    lo, hi = 0, len(a) - 1
    print("mid: ", end="")
    while lo <= hi:
        mid = (lo + hi) // 2
        print(mid, end=", ")
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
    
print(f"index {binary_search(A, target)}")