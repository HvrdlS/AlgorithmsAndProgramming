import random, time

A = [random.randint(1, 100) for _ in range(2000)]


def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        mi = i
        for j in range(i + 1, n):
            if a[j] < a[mi]:
                mi = j
        a[i], a[mi] = a[mi], a[i]
    return a
    
    
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
    

def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:          # already sorted — exit
            break
    return a
    
    
def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
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
    
    
def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)
    
def benchmark(sort_func, data):
    start = time.perf_counter()
    result = sort_func(data.copy())
    end = time.perf_counter()

    return result, end - start


for sort_func in [selection_sort, insertion_sort, bubble_sort, merge_sort, quick_sort, sorted]:
    result, time_elapsed = benchmark(sort_func, A)
    print(f"{sort_func.__name__}: {time_elapsed} seconds")
    
