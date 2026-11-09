A = [5, 2, 9, 1, 5, 6]        
B = [1, 2, 3, 4, 5]           
C = [5, 4, 3, 2, 1]          
D = []                       
E = [7]    

def merge_sort(a, depth = 0):
    print(f"depth {depth} {a}")
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid], depth + 1)
    right = merge_sort(a[mid:], depth + 1)
    return merge(left, right)


def merge(x, y):
    res, i, j = [], 0, 0
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            res.append(x[i]); i += 1
        else:
            res.append(y[j]); j += 1
    res += x[i:] + y[j:]
    return res
    
for test in [A, B, C, D, E]:
    print(f"\n {merge_sort(test.copy())}")