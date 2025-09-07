def cm2_to_m2(area_cm2: float)-> float:
    "Convert area from square centimeters to square meters."
    return area_cm2 / 10000

def m2_to_cm2(area_m2: float)-> float:
    "Convert area from square meters to square centimeters."
    return area_m2 * 10000

def larger_shape(shape1, shape2):
    "Return the shape with the larger area."
    if shape1.area() > shape2.area():
        return shape1
    else:
        return shape2
    


