"""Data types: list of words, dictionary, and sorted key-value pairs.
The list supports sequential splitting, the dictionary provides average
O(1) frequency updates, and sorting u distinct words costs O(u log u).
"""

import re
text = "an algorithm is a sequence of steps an algorithm must be finite"
words = re.split(r'\s+', text.strip())
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1 
    else: 
        freq[word] = 1 
result = sorted(freq.items(), key=lambda item: item[1])  
for word, count in result:
    if count > 1:
         print(f"{word}: {count}")