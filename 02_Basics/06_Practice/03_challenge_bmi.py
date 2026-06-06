"""
Challenge: BMI Calculator

Build a BMI (Body Mass Index) calculator.
BMI = weight(kg) / height(m)^2

Categories:
- Below 18.5: Underweight
- 18.5 - 24.9: Normal
- 25 - 29.9: Overweight
- 30 and above: Obese
"""

print("=== BMI Calculator ===")

# Get user info
name = input("Your name: ")
weight = float(input("Weight in kg: "))
height = float(input("Height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)
bmi_rounded = round(bmi, 1)

# Determine category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Display results
print(f"\n{name}'s BMI Results:")
print(f"BMI: {bmi_rounded}")
print(f"Category: {category}")
