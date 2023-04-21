# Create a class called Rectangle that has attributes width and height.
# Add methods str and repr that return a string representation of the rectangle object.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # def __str__(self):
    #     return f"This rectangle is {self.height}m high and {self.width}m wide."

    def __repr__(self):
        return f"Rectangle\n\tHeight: {self.height}m\n\tWidth: {self.width}m"


rectangle = Rectangle(10, 25)
print(rectangle)
