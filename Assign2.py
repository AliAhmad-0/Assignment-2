Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")


2:Write a program that calculates the volume of a cylinder using the formula?

# Volume of Cylinder Calculation Program
radius = float(input("Enter the radius of the cylinder in meters: "))
height = float(input("Enter the height of the cylinder in meters: "))

volume = math.pi * (radius ** 2) * height

print(f"The volume of the cylinder is: {volume:.2f} cubic meters")