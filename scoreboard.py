from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(
            arg="Score: " + str(self.score),
            move=False,
            align="center",
            font=("Arial", 15, "bold"),
        )

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(
            arg="Score: " + str(self.score),
            move=False,
            align="center",
            font=("Arial", 15, "bold"),
        )

    def gameover(self):

        self.goto(0, 0)

        self.write("GAME OVER", move=False, align="center", font=("Arial", 15, "bold"))
