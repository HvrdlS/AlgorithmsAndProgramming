weight, ticketclass = int(input("Enter the weight(kg): ")), str(input("Enter the class(econom, business): "))
cost = 15
if weight <= 0: print(f"No weight/error")
else:
    if ticketclass == "econom": 
        if 0 < weight <= 20: surcharge = 0
        else: surcharge = cost * (weight - 20)
    else:
        if 0 < weight <= 30: surcharge = 0
        else: surcharge = cost * (weight - 30)
    print(f"{ticketclass} - {surcharge} UAH")
weight = 20
assert weight <= 20
weight = 25
assert 15 * (weight - 20) == 75
weight = 35
assert 15 * (weight - 30) == 75
weight = 0
assert weight <= 0