from turtle import Turtle


class Snake:
    def __init__(self, starting_length=3):
        self.snakeBody = []
        for i in range(0, starting_length):
            new_body = Turtle()
            new_body.shape("square")
            new_body.color("white")
            new_body.penup()
            self.snakeBody.append(new_body)
            self.snakeBody[i].setpos(x=i * -20, y=0)

    def move(self):
        for body in range(len(self.snakeBody) - 1, 0, -1):
            new_x = self.snakeBody[body - 1].xcor()
            new_y = self.snakeBody[body - 1].ycor()
            self.snakeBody[body].goto(new_x, new_y)

        self.snakeBody[0].forward(20)
