import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # This code makes a new Turtle. Pick a new name for the turtle
    Dan = turtle.Turtle()
    Dan.shape('turtle')
    # Make your turtle's shape 'turtle', .shape('turtle')
    Dan.speed(2)
    # Set your turtle's speed using .speed(2)
    Dan.color('green')
    # Set your turtle's color using .color('green') and .pencolor('blue')
    Dan.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    Dan.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    Dan.right(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for i in range(4):
        Dan.right(90)
        Dan.forward(100)
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    Dan.goto(x= 0, y= 0)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    Dan.begin_fill()
    Dan.circle(30, steps=30)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    Dan.end_fill()
    # Draw 3 more shapes with different fill colors!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
