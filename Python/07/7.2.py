s = str(input("Enter the text: "))
vowels = 0
consonants = 0
others = 0
letters = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяabcdefghijklmnopqrstuvwxyz"
ukrainian_vowels = "аеєиіїоуюя"
latin_vowels = "aeiou"
for c in s:
    letter = c.lower()
    if letter in letters:
        if letter in ukrainian_vowels or letter in latin_vowels:
            vowels += 1
        else:
            consonants += 1
    else:
        others += 1
print(f"vowels: {vowels}, consonants: {consonants}, others: {others}")