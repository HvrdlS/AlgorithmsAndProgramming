a = list(map(int, input("Input the numbers: ").split()))
b = list(map(int, input("Input the numbers: ").split()))
a_ind = 0
b_ind = 0
result = []  
while a_ind < len(a) and b_ind < len(b):
    if a[a_ind] < b[b_ind]: 
        result.append(a[a_ind])
        a_ind += 1
    else: 
        result.append(b[b_ind]) 
        b_ind += 1
if a_ind == len(a): result.extend(b[b_ind:])
else: result.extend(a[a_ind:])
print(result)