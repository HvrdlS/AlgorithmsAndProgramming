s = str(input("Enter the text: ")) 
char = input("Enter the character: ")
i = 0
count = 0
indices = ""
for c in s:
    if c == char:
        count += 1
        indices += str(i) + " "
    i += 1
print(f"{char} = {count} times, indices {indices}")   