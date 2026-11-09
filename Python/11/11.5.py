A = [5, 2, 9, 1, 5, 6]  # worst case because it is the most unbalanced
B = [1, 2, 3, 4, 5]           
C = [5, 4, 3, 2, 1]          
D = []                       
E = [7]    

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)
    
for test in [A, B, C, D, E]:
    print(f"{quick_sort(test.copy())}")