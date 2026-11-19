text = "an algorithm is a sequence of steps an algorithm must be finite"
words = text.split()
freq = {}
for word in words:
    if word != " ":
        if word in freq:
            freq[word] += 1 
        else: 
            freq[word] = 1 
result = sorted(freq.items(), key=lambda item: item[1])  
for word, count in result:
    if count > 1:
         print(f"{word}: {count}")