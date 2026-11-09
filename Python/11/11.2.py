A = [5, 2, 9, 1, 5, 6]        
B = [1, 2, 3, 4, 5]           
C = [5, 4, 3, 2, 1]          
D = []                       
E = [7]     

def insertion_sort(a):
    operations = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        operations += 2
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            operations += 2
        a[j + 1] = key
        operations += 1
    return a, operations 

for test in [A, B, C, D, E]:
    result, operations = insertion_sort(test.copy())
    print(f"{result}, operations {operations}")
    
print("Insertion sort works from left to right, inserting each element into its correct position among the previously sorted elements. Already sorted lists require fewer operations, while reverse-sorted lists require more shifts because each new element must move to the beginning.")