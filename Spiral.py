import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 0
while True:
    for i in range(9):
        my_pen.forward(size + 1)
        my_pen.left(40)
        size = size - 5
    size = size + 1