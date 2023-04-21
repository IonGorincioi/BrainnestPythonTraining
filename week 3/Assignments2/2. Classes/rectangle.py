# Create a class called Rectangle that has attributes width and height.
# Add methods area and perimeter that calculate the area and perimeter
# of the rectangle, respectively.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        rectangle_area = self.width * self.height
        return rectangle_area

    def perimeter(self):
        rectangle_perimeter = 2 * (self.width + self.height)
        return rectangle_perimeter


rectangle1 = Rectangle(10, 20)
print(f"Area: {rectangle1.area()}")
print(f"Perimeter: {rectangle1.perimeter()}")
