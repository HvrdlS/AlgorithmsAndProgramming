"""Data types: string, dictionary, and list of sorted key-value pairs.
The dictionary gives average O(1) character-count updates; sorting has
O(u log u) time for u distinct characters, with O(n) overall counting.
"""

import re
a = "abr  acada  bra"
freq = {}
result = re.sub("\s+","",a)
for char in result:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1 

result = sorted(freq.items(), key=lambda item: item[1], reverse = True)[:3]
print(a)
for char, count in result:
    print(f"{char}={count}")