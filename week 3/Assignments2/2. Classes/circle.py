# Create a class called Circle that has attribute radius.
# Add methods area and circumference that calculate the
# area and circumference of the circle, respectively.

import math


class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        circle_length = 2 * self.PI * self.radius
        return circle_length

    def disc_area(self):
        area = self.PI * math.pow(self.radius, 2)
        return area


circle1 = Circle(1)
print(circle1.circumference())
print(circle1.disc_area())