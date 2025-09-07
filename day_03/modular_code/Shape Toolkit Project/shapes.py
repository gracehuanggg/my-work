class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    def area(self) -> float:
        return self.width * self.height
    def describe(self):
        print(f"Rectangle {self.width} by {self.height} has area {self.area()} cm^2")
rect_1 = Rectangle (10,5)
rect_1.describe()
print (f"Area of rectangle is {rect_1.area()} cm^2")
rect_2 = Rectangle (3,7)
rect_2.describe()
print (f"Area of rectangle is {rect_2.area()} cm^2")

class circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14
    def area(self) -> float:
        return self.radius * self.radius * self.pi
    def describe(self):
        print (f"Circle with radius {self.radius} has area {self.area()} cm^2")
circle_1 = circle (5)
circle_1.describe()
print (f"Area of circle is {circle_1.area()} cm^2")
circle_2 = circle (10)
circle_2.describe()
print (f"Area of circle is {circle_2.area()} cm^2")

class triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self) -> float:
        return 0.5 * self.base * self.height
    def describe(self):
        print (f"Triangle with base {self.base} and height {self.height} has area {self.area()} cm^2")
triangle_1 = triangle (10,5)
triangle_1.describe()
print (f"Area of triangle is {triangle_1.area()} cm^2")
triangle_2 = triangle (3,7)
triangle_2.describe()
print (f"Area of triangle is {triangle_2.area()} cm^2")