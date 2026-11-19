age = int(input("Enter the age: "))
sex = str(input("Enter the sex(m, f): "))
status = "No"

if sex != "m" and sex != "f": 
    print(f"Wrong sex")
else:   
    if age <= 0: 
        print(f"Wrong age")
    else:      
        if age < 18:
            status = "Yes"
        else:
            if sex == "f":
                if age >= 60:
                    status = "Yes"
            else: 
                if age >= 65:
                    status = "Yes"
        print(f"{age} {sex} - {status}")
        
age, sex = 17, "m"
assert age < 18
age, sex = 60, "f"
assert sex == "f" and age >= 60
age, sex = 65, "m"
assert sex == "m" and age >= 65
age, sex = 0, "f"
assert age <= 0