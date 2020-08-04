import turtle
if __name__ == '__main__':
    window = turtle.Screen()
    Dave = turtle.Turtle()
    Dave.shape('turtle')
    for i in range(4):
        Dave.forward(100)
        Dave.right(90)
        for k in range(4):
                Dave.forward(100)
                Dave.right(90)
    turtle.done()
