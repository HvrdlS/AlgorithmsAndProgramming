x, y = map(int, input("Enter two coordinates(x, y): ").split())
if x == 0 or y == 0:
    if x == 0 and y == 0: 
        print(f"Origin")
    elif y == 0: 
        print(f"OX axis")
    elif x == 0: 
        print(f"OY axis")  
else:  
    if x > 0 and y > 0:     
        print(f"First quadrant")
    elif x < 0 and y > 0:
        print(f"Second quadrant")
    elif x < 0 and y < 0:
        print(f"Third quadrant")
    else: print(f"Fourth quadrant")