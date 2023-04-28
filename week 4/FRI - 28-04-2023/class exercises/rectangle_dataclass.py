# Create a dataclass called Rectangle with the following attributes:
# length (float), width (float), color (str). Write a method called
# area that returns the area of the rectangle. Instantiate an object
# of Rectangle with a length of 5.0, width of 3.0, and color of "blue",
# and print out its area.

from dataclasses import dataclass


@dataclass
class Rectangle():
    length: float
    width: float
    color: str

    def area(self):
        return self.length * self.width


rectangle1 = Rectangle(5, 3, "blue")
print(rectangle1)
print(f"Area: {rectangle1.area()} m.sq.")