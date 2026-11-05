import math
mass, height = map(float, input("Enter the mass(kg) and height(m): ").split())
BMI = mass / height ** 2
print(f"BMI = {BMI:.2f}")