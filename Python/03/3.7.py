import math
deposit, annual_rate = map(float, input("Enter the deposit amount and annual interest rate(%): ").split())
years = 3
final_amount = deposit * (1 + (annual_rate / 100)) ** years
print(f"{final_amount:.2f}")