# import colorgram
#
# # Extract 7 colors from image
# colors = colorgram.extract('Colorgram.jpeg', 30)
#
# # New list
# rgb_colors = []
#
# # Get the color code
# for color in colors:
#     # Color.rgb - The color represented as a namedtuple of RGB from 0 to 255 ie. (r=255, g=151, b=210)
#     # Get individual colors and put it in r or g or b
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle
import random

t = Turtle()
screen = turtle.Screen()
t.speed("fastest")

color_list = [(14, 119, 185), (206, 138, 168), (199, 175, 9), (240, 213, 62), (220, 156, 97), (150, 17, 34), (122, 72, 100), (13, 143, 53), (74, 29, 35), (59, 34, 31), (204, 67, 26), (226, 170, 199), (242, 80, 27), (16, 172, 189), (34, 176, 93), (2, 114, 63), (247, 214, 2), (114, 188, 142), (181, 95, 111), (188, 182, 211), (40, 39, 46), (157, 207, 217), (229, 173, 162), (162, 208, 181), (118, 117, 163)]
t.screen.title('Playing with Turtle')

# Setting the screen color-mode
screen.colormode(255)

# print(t.pos())
# t.dot(20, "pink")
# t.penup()
# t.forward(50)
# t.pendown()
# t.dot(20)
# print(t.pos())

for _ in range(10):
    random_color = random.choice(color_list)
    t.dot(20, random_color)
    t.penup()
    t.forward(50)
    t.pendown()


screen.exitonclick()

