import turtle
import random

# CALL TO DRAW
def draw_polygon(num_sides, size, orientation, location, color, border_size):
    # stop make line
    turtle.penup()
    # random where to place new picture
    turtle.goto(location[0], location[1])
    # set direction
    turtle.setheading(orientation)
    # set color
    turtle.color(color)
    # set borderline
    turtle.pensize(border_size)
    # Real drawing step
    # start drawing
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

# random color
def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# ????????????????
turtle.speed(0)
#background color
turtle.bgcolor('black')
# ????????????????
turtle.tracer(0)
# color model
turtle.colormode(255)

################ DRAW ONE SHAPE #######################################
# draw a polygon at a random location, orientation, color, and borderline thickness

# 1. Random data
num_sides = random.randint(3, 5) # triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = get_new_color()
border_size = random.randint(1, 10)
# 2. Draw
draw_polygon(num_sides, size, orientation, location, color, border_size)

################ DRAW INNER SHAPE #######################################
# specify a reduction ratio to draw a smaller polygon inside the one above
## increase smaller / decrease bigger
reduction_ratio = 0.618
# reposition the turtle and get a new location
turtle.penup()
turtle.forward(size*(1-reduction_ratio)/2)
turtle.left(90)
turtle.forward(size*(1-reduction_ratio)/2)
turtle.right(90)

# move to draw inner position ??
# ???
location[0] = turtle.pos()[0]
location[1] = turtle.pos()[1]
# adjust the size according to the reduction ratio
size *= reduction_ratio
# draw the second polygon embedded inside the original 
draw_polygon(num_sides, size, orientation, location, color, border_size)



# hold the window; close it by clicking the window close 'x' mark
turtle.done()