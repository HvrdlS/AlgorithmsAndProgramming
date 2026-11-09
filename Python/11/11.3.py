A = [5, 2, 9, 1, 5, 6]        
B = [1, 2, 3, 4, 5]           
C = [5, 4, 3, 2, 1]          
D = []                       
E = [7]     

def bubble_sort(a):
    n = len(a)
    passes = 0
    for i in range(n - 1):
        swapped = False
        passes += 1
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:     
            break
    return a, passes
    
for test in [A, B, C, D, E]:
    result, passes = bubble_sort(test.copy())
    print(f"{result}, passes {passes}")