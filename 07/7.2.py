s = str(input("Enter the text: "))
vowels = 0
consonants = 0
others = 0
for c in s:
    if c.isascii() and c.isalpha():
        if c.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    else:
        others += 1
print(f"vowels: {vowels}, consonants: {consonants}, others: {others}")