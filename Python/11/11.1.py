A = [5, 2, 9, 1, 5, 6]        
B = [1, 2, 3, 4, 5]           
C = [5, 4, 3, 2, 1]          
D = []                       
E = [7]                      

def selection_sort(a):
    n = len(a)
    swaps = 0
    comparisons = 0
    for i in range(n - 1):
        mi = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[mi]:
                mi = j
        if mi != i:
            swaps += 1
            a[i], a[mi] = a[mi], a[i]
    return a, comparisons, swaps
    
for test in [A, B, C, D, E]:
    result, comparisons, swaps = selection_sort(test.copy())
    print(f"{result}, comparisons {comparisons}, swaps {swaps}")