import math

print()
width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

print()

volume = float((math.pi * (width **2) * ratio * ((width * ratio) + (2540 * diameter))) / 10000000000)

print(f"The approximate volume is {volume:.2f} liters.")
print()