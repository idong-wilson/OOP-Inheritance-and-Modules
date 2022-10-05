import math
# Calculating the area of a circle with radius
radius = float(input("Enter the radius: "))

area = str(math.pi * radius**2)

print(f"Area of a circle with radius {radius} is {area} cm")

# Finding the Hypothenus of a right angled triangle

print("Enter the length of the shorter sides of the triangle:")

a = float(input("Enter a: "))
b = float(input("Enter b: "))

c = math.sqrt(a ** 2 + b ** 2)
print("The Hypothenus of the triangle is", c)