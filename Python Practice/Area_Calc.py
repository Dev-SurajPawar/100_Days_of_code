import math

def paint_calc(height, width, cover):

    area = height * width
    number_of_cans  = math.ceil(area / cover)
    print(f"You'll need {number_of_cans} cans of paint")



h = int(input("Height of wall: "))
w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=h, width=w, cover=coverage)