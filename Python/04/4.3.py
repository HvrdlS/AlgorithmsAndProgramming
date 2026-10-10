minutes = int(input("Enter the number of minutes: " ))
day = minutes // 1440
hours = (minutes % 1440) // 60
min = minutes % 60
print(f"{day} day(s) {hours} h {min} min")