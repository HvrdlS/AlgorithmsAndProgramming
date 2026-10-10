cm = int(input("Enter the number of centimeters: "))
m = cm // 100
remaining_cm = cm % 100
inches = cm // 2.54
print(f"{m} m {remaining_cm:02d} cm, {inches:.2f} inches")