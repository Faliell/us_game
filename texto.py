import turtle


class Texto(turtle.Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(arg=f'{state}', align='center', font=('Arial', 10, 'normal'))
