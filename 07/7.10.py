s = input("Enter the text: ")
counts = {}
for c in s:
    if c.isspace():
        pass
    elif c in counts:
        counts[c] += 1
    else: counts[c] = 1
longest = max(counts, key=counts.get)
print(longest, counts[longest])