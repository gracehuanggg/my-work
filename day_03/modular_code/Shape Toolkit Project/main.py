from shapes import Rectangle, circle, triangle
from utils import cm2_to_m2, m2_to_cm2, larger_shape

def welcome_message ()-> None:
    print ("Welcome to the Shape Toolkit Project!")
    print("We support Rectangles, Circles, and Triangles.")
    print("let's see some examples...")

def read_positive_number(prompt_text):
    while True:
        text = input(prompt_text)
        try:
            value = float(text)
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("That wasn't a number. Try again.")

def user_create_shape():
    print("Choose a shape type: rectangle / circle / triangle")
    shape_type = input("Type: ").strip().lower()

    if shape_type == "rectangle":
        w = read_positive_number("Width (cm): ")
        h = read_positive_number("Height (cm): ")
        return Rectangle(w, h)

    elif shape_type == "circle":
        r = read_positive_number("Radius (cm): ")
        return Circle(r)

    elif shape_type == "triangle":
        b = read_positive_number("Base (cm): ")
        h = read_positive_number("Height (cm): ")
        return Triangle(b, h)

    else:
        print("Please enter rectangle, circle, or triangle.")
        return None

def main():
    welcome_message()

    shapes = []

    while True:
        how_many_text = input("How many shapes would you like to add? ")
        try:
            how_many = int(how_many_text)
            if how_many >= 1:
                break
            else:
                print("Please enter a number 1 or greater.")
        except ValueError:
            print("Please enter a whole number like 1, 2, or 3.")

    for i in range(how_many):
        print("Adding shape", i)
        s = create_shape_from_user()
        if s is not None:
            shapes.append(s)
            print("Added!")
        else:
            print("Shapes are not added.")

    if len(shapes) == 0:
        print("\nNo shapes to show. Goodbye!")
        return

    print("\nYour shapes and areas:")
    i = 0
    while i < len(shapes):
        s = shapes[i]
        print("Index", i, "->")
        s.describe()
        area_cm2 = s.area()
        area_m2 = cm2_to_m2(area_cm2)
        print("Area in square meters:", area_m2, "m^2")
        print("Area in cm^2:", m2_to_cm2(area_m2), "cm^2")
        print()
        i += 1




