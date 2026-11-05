s = str(input("Enter the text: ")) 
title = s.title()
abbreviation = ""
for c in title:
    if c.isupper():
        abbreviation += c
print(title, abbreviation)