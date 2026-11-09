A = [5, 2, 9, 1, 5, 6]       
B = [1, 2, 3, 4, 5]          
C = [5, 4, 3, 2, 1]           
D = []                       
E = [7]
F= [-5, 2, -1, 3]

def selection_sort_descending(a):
    n = len(a)
    for i in range(n - 1):
        mi = i
        for j in range(i + 1, n):
            if a[j] > a[mi]:
                mi = j
        a[i], a[mi] = a[mi], a[i]
    return a
 
def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        mi = i
        for j in range(i + 1, n):
            if abs(a[j]) < abs(a[mi]):
                mi = j
        a[i], a[mi] = a[mi], a[i]
    return a 
    
for test in [A,B,C,D,E]:
    print(f"{selection_sort_descending(test.copy())}")
    
print(selection_sort(F))   