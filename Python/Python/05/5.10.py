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