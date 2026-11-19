a = input("First word: ").lower()
b = input("Second word: ").lower()

freq_a = {}
freq_b = {}

for char in a:
    freq_a[char] = freq_a.get(char, 0) + 1

for char in b:
    freq_b[char] = freq_b.get(char, 0) + 1

print(freq_a == freq_b)