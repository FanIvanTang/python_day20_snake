from turtle import Turtle

MOVE_DISTANCE = 20
BODY_SIZE = 20
INITIAL_LEN_OF_BODY = 3


class Snake:

    body = []

    def __init__(self):

        for i in range(INITIAL_LEN_OF_BODY):

            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(-BODY_SIZE * i, 0)
            self.body.append(t)

        self.head = self.body[0]

    def eat_food(self):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.speed("fastest")

        if self.head.heading() == 0:
            x = self.head.pos()[0] + 20
            y = self.head.pos()[1]
        elif self.head.heading() == 180:
            x = self.head.pos()[0] - 20
            y = self.head.pos()[1]
        elif self.head.heading() == 90:
            x = self.head.pos()[0]
            y = self.head.pos()[1] + 20
        elif self.head.heading() == 270:
            x = self.head.pos()[0]
            y = self.head.pos()[1] - 20
        t.goto(x, y)
        t.setheading(self.head.heading())
        self.body.insert(0, t)
        self.head = self.body[0]

    def move(self):

        l = len(self.body)

        for i in range(l - 1, 0, -1):

            x = self.body[i - 1].pos()[0]
            y = self.body[i - 1].pos()[1]

            self.body[i].goto(x, y)

        self.head.fd(MOVE_DISTANCE)

    def up(self):

        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(270)

    def left(self):

        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(0)
