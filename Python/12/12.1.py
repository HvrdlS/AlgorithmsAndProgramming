a = "abracadabra"
freq = {}
for char in a:
    if char != " ":
       if char in freq:
           freq[char] += 1
       else:
            freq[char] = 1 

result = sorted(freq.items(), key=lambda item: item[1], reverse = True)[:3]
print(a)
for char, count in result:
    print(f"{char}={count}")