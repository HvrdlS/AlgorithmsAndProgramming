"""Data types: strings and dictionaries.
Dictionaries count character frequencies with average O(1) updates;
comparing the two dictionaries and scanning both words takes O(n + m) time
for words of lengths n and m.
"""

a = input("First word: ").lower()
b = input("Second word: ").lower()

freq_a = {}
freq_b = {}

for char in a:
    freq_a[char] = freq_a.get(char, 0) + 1

for char in b:
    freq_b[char] = freq_b.get(char, 0) + 1

print(freq_a == freq_b)