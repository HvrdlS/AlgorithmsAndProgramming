s = str(input("Enter the text: ")) 
newstring = ""
count = 0
for c in s:
    if c.isdigit():
        newstring += "#"
        count += 1
    else: 
        newstring += c
print(newstring)
print("Replacements: ", count)