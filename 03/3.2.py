a = int(input("Enter the number: "))
hour = a // 3600
minute =(a % 3600) // 60
second = a % 60
print (f"{hour}:{minute:02d}:{second:02d}")