month = int(input("Enter the month number: "))
if month > 12 or month < 1: print(f"Error")
elif 1 <= month <= 2 or month == 12: print(f"Winter")
elif 3 <= month <= 5: print(f"Spring")
elif 6 <= month <= 8: print(f"Summer")
elif 9 <= month <= 11: print(f"Autumn")

month = 12
assert month == 12
month = 4
assert 3 <= month <= 5
month = 8
assert 6 <= month <= 8
month = 13
assert month > 12