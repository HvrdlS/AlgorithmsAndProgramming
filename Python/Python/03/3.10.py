minutes, price, VAT = map(float, input("Enter the number of minutes, price per minute and VAT(%): ").split())
total_cost = minutes * price
VAT_amount = total_cost * (VAT / 100)
final_cost = total_cost + VAT_amount
print(f"Without VAT: {total_cost:.2f}, VAT: {VAT_amount:.2f}, Total: {final_cost:.2f}")