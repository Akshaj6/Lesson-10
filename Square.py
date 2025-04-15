import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("green")
screen.title("The Square")
side_length = 100
for i in range(4):
    t.forward(side_length)
    t.right(90)
turtle.done()