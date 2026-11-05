s = input("Enter the text: ")
k = int(input("Enter the integer: "))
newstr = ""
for c in s:
    if c.isupper():
        currentchar = ord(c)
        newstr += chr((currentchar - 65 + k) % 26 + 65)
    elif c.islower():
        currentchar = ord(c)
        newstr += chr((currentchar - 97 + k) % 26 + 97)
    else:
        newstr += c
print(newstr)