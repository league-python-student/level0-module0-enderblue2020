import random
import turtle

# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    Dave = turtle.Turtle()
    # This code sets our shape to a turtle
    Dave.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    Dave.speed(10)
    # Set your turtle's color using .color('green')
    Dave.color('green')
    # Use a loop to repeat a the code below 50 times
    for i in range(95):
        # Set the turtle color to a random color
        Dave.color(getRandomColor())
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        Dave.forward(5*i)
        # Turn the turtle (360/7) degrees to the right
        Dave.right(360/7)
        # Change the turtle width to 'i' (the loop variable)
        Dave.width(i)
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
