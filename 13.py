from abc import ABC, abstractmethod

# Step 1: Define the abstract Shape class
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Step 2: Implement Concrete Shape Classes (Circle, Square, Rectangle)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        return f"Drawing a Circle with radius {self.radius}"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def draw(self):
        return f"Drawing a Square with side {self.side}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        return f"Drawing a Rectangle with width {self.width} and height {self.height}"

# Step 3: Implement the ShapeFactory
class ShapeFactory:
    def create_shape(self, shape_type, *args):
        if shape_type == "Circle":
            return Circle(*args)
        elif shape_type == "Square":
            return Square(*args)
        elif shape_type == "Rectangle":
            return Rectangle(*args)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Step 4: Using the factory to create shapes
if __name__ == "__main__":
    # Create an instance of ShapeFactory
    factory = ShapeFactory()

    # Generate different shapes using the factory
    shapes = [
        factory.create_shape("Circle", 5),  # Circle with radius 5
        factory.create_shape("Square", 4),  # Square with side 4
        factory.create_shape("Rectangle", 3, 6)  # Rectangle with width 3 and height 6
    ]

    # Call the draw() method for each shape
    for shape in shapes:
        print(shape.draw())
