A = [5, 2, 9, 1, 5, 6]       

target = int(input("Enter the target: "))

def linear_search(a, target):
    comparisons = 0
    for i, x in enumerate(a):
        comparisons += 1
        if x == target:
            return i, comparisons 
    return -1, comparisons 


result, comparisons = linear_search(A, target)
print(f"A, {target} - index {result}, comparisons {comparisons}")