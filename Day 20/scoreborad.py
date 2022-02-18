from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Python\#100DaysOfCode\Day 20\data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 275)
        self.pendown()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score = {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Python\#100DaysOfCode\Day 20\data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
