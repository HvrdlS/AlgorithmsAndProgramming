A = [5, 2, 9, 1, 5, 6]        
B = [1, 2, 3, 4, 5]           
C = [5, 4, 3, 2, 1]          
D = []                       
E = [7]     

def bubble_sort(a):
    comparisons = 0
    swaps = 0
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return a, comparisons, swaps
    
for test in [A, B, C, D, E]:
    result, comparisons, swaps = bubble_sort(test.copy())
    print(f"{result}, comparisons {comparisons}, swaps {swaps}")

print("Bubble sort repeatedly compares neighboring elements and moves larger elements to the end. In a sorted list it stops early, while quick sort uses a pivot and recursively partitions the remaining elements.")