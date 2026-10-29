s = str(input("Enter the text: "))
t= "".join(c.lower() for c in s if c.isalnum())
print(t == t[::-1])