import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


# take input from user
r = float(input("Enter the radius: "))

# create object
c = Circle(r)

# display results
print("Area of circle:", c.area())
print("Perimeter of circle:", c.perimeter())