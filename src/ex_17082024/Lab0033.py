# find area of circle given the radius
# Logic building steps
# step1: For any program, sort out inputs and outputs
# step2: write the rough logic
# step3: Build the logic

import math

radius  = float(input("Enter the radius: "))
area = math.pi*math.pow(radius,2)
area2 = 3.14 * (radius**2)
print("Area of the circle is: ", area)
print(f"Area of the circle is: {area:.2f}")
print("area2", area2)


