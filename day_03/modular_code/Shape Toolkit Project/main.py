from shapes import Rectangle, circle, triangle
from utils import cm2_to_m2, m2_to_cm2, larger_shape

def welcome_message ()-> None:
    print ("Welcome to the Shape Toolkit Project!")
    print("We support Rectangles, Circles, and Triangles.")
    print("let's see some examples...")

welcome_message()

rect_1 = Rectangle (20,20)
circle_1 = circle (7)
triangle_1 = triangle (10,5)


def main():
    welcome_message()

shapes = [
        Rectangle(20, 20),
        circle(7),
        triangle(10, 5)
]
for shape in shapes:
    shape.describe()
    area_cm2 = shape.area()
    area_m2 = cm2_to_m2(area_cm2)
    print(f"Area in square meters: {area_m2} m^2")
    area_cm2_converted = m2_to_cm2(area_m2)
    print(f"Converted back to square centimeters: {area_cm2_converted} cm^2")



# Compare two shapes
bigger = larger_shape(shapes[0],shapes[1])
print(f"The shape with the larger area is: {bigger.describe()}")
bigger.describe()





