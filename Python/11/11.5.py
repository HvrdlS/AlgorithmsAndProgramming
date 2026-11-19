A = [5, 2, 9, 1, 5, 6]        
B = [1, 2, 3, 4, 5]           
C = [5, 4, 3, 2, 1]          
D = []                       
E = [7]    

comparisons = 0
swaps = 0

def quick_sort(a):
    global comparisons, swaps
    if len(a) <= 1:
        return a

    pivot = a[len(a) // 2]
    less = []
    equal = []
    greater = []

    for x in a:
        comparisons += 1
        if x < pivot:
            less.append(x)
            swaps += 1
        elif x > pivot:
            greater.append(x)
            swaps += 1
        else:
            equal.append(x)

    return quick_sort(less) + equal + quick_sort(greater)

for test in [A, B, C, D, E]:
    comparisons = 0
    swaps = 0
    result = quick_sort(test.copy())
    print(f"{result}, comparisons {comparisons}, swaps {swaps}")

print("Quick sort uses a pivot to divide the list into smaller and larger parts, then sorts each part recursively. Bubble sort repeatedly compares and swaps neighboring elements, while quick sort partitions the list around a pivot.")