class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    def area(self) -> float:
        return self.width * self.height
    def describe(self):
        print(f"Rectangle {self.width} by {self.height} has area {self.area()} cm^2")

class circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14
    def area(self) -> float:
        return self.radius * self.radius * self.pi
    def describe(self):
        print (f"Circle with radius {self.radius} has area {self.area()} cm^2")

class triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self) -> float:
        return 0.5 * self.base * self.height
    def describe(self):
        print (f"Triangle with base {self.base} and height {self.height} has area {self.area()} cm^2")
