import random
import turtle as t

first = t.Turtle()
# print(first)
# first.shape("turtle")
# first.color("coral")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

direction = [0, 90, 180, 270]
first.pensize(15)
first.speed("fastest")

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         first.forward(100)
#         first.left(angle)
#
# for shap_side_n in range(3,11):
#     first.color(random.choice(colors))
#     draw_shape(shap_side_n)

for _ in range(200):
    first.color(random_color())
    first.forward(30)
    first.setheading(random.choice(direction))