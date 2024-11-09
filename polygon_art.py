import turtle
import random


class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size
    def draw(self):
        turtle.penup()
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()
    def move(self):
        turtle.goto(self.location[0], self.location[1])

class PolygonArt:
    def __init__(self, user_choice):
        self.user_choice = user_choice
    def run(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        times = random.randint(20,30)
        if self.user_choice == "1":
            for i in range(times) :
                num_sides = 3
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                polygon = Polygon(num_sides, size, orientation, location, color,border_size)
                polygon.move()
                polygon.draw()
        if self.user_choice == "2":
            for i in range(times) :
                num_sides = 4
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                polygon = Polygon(num_sides, size, orientation, location, color,border_size)
                polygon.move()
                polygon.draw()
        if self.user_choice == "3":
            for i in range(times) :
                num_sides = 5
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                polygon = Polygon(num_sides, size, orientation, location, color,border_size)
                polygon.move()
                polygon.draw()
        if self.user_choice == "4":
            for i in range(times) :
                num_sides = random.randint(3, 5)
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                polygon = Polygon(num_sides, size, orientation, location, color,border_size)
                polygon.move()
                polygon.draw()
        if self.user_choice == "5":
            for i in range(times) :
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                polygon = Polygon(3, size, orientation, location, color,border_size)
                polygon.move()
                polygon.draw()
                inner_polygon = EmbeddedPolygon(3, size, orientation, location, color,border_size)
                inner_polygon.draw()
        if self.user_choice == "6":
            for i in range(times) :
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                polygon = Polygon(4, size, orientation, location, color,border_size)
                polygon.move()
                polygon.draw()
                inner_polygon = EmbeddedPolygon(4, size, orientation, location, color,border_size)
                inner_polygon.draw()
        if self.user_choice == "7":
            for i in range(times) :
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                polygon = Polygon(5, size, orientation, location, color,border_size)
                polygon.move()
                polygon.draw()
                inner_polygon = EmbeddedPolygon(5, size, orientation, location, color,border_size)
                inner_polygon.draw()
        if self.user_choice == "8":
            for i in range(times) :
                num_sides = random.randint(3, 5)
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                polygon = Polygon(num_sides, size, orientation, location, color,border_size)
                polygon.move()
                polygon.draw()
                inner_polygon = EmbeddedPolygon(num_sides, size, orientation, location, color,border_size)
                inner_polygon.draw()
        if self.user_choice == "9":
            for i in range(times):
                random_choice = random.randint(1,2)
                if random_choice == 1 :
                    num_sides = random.randint(3, 5)
                    size = random.randint(50, 150)
                    orientation = random.randint(0, 90)
                    location = [random.randint(-300, 300), random.randint(-200, 200)]
                    color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                    border_size = random.randint(1, 10)
                    polygon = Polygon(num_sides, size, orientation, location, color, border_size)
                    polygon.move()
                    polygon.draw()
                else :
                    num_sides = random.randint(3, 5)
                    size = random.randint(50, 150)
                    orientation = random.randint(0, 90)
                    location = [random.randint(-300, 300), random.randint(-200, 200)]
                    color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                    border_size = random.randint(1, 10)
                    polygon = Polygon(num_sides, size, orientation, location, color,border_size)
                    polygon.move()
                    polygon.draw()
                    inner_polygon = EmbeddedPolygon(num_sides, size, orientation, location, color,border_size)
                    inner_polygon.draw()

class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, border_size,
                 num_levels=2, reduction_ratio = 0.618):
        Polygon.__init__(self, num_sides, size, orientation, location, color, border_size)
        self.num_levels = num_levels
        self.reduction_ratio = reduction_ratio
    def draw(self):
        for i in range(self.num_levels):
            turtle.penup()
            turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]
            self.size *= self.reduction_ratio
            inner_porygon = Polygon(self.num_sides, self.size, self.orientation,
                                    self.location, self.color, self.border_size)
            inner_porygon.draw()


choice = input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: ")
Art_piece = PolygonArt(choice)
Art_piece.run()

turtle.done()