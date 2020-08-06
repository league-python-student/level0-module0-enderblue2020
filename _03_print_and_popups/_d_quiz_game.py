from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    userscore = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    answer1 = simpledialog.askstring(title='question', prompt='How fast was the Cutty Sark (in knots).')
    #      // 3.  Use an if statement to check if their answer is correct
    if answer1 == '17.5':
        messagebox.showinfo(title=None, message='The Cutty Sark was a clipper ship, so its pretty fast.')
    else:
        messagebox.showinfo(title=None, message='Wrong. Its 17.5 knots')
    #      // 4.  if the user's answer was correct, add one to their score 
    if answer1 == '17.5':
        userscore = userscore + 1
    else:
        userscore = userscore - 1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    answer2 = simpledialog.askstring(None, prompt="At five foot four, George Washington was the shortest president.")
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    if answer2 == 'false':
        messagebox.showinfo(None, message="George Washington was actually 6 foot 4, tall for people in those days.")
    else:
        messagebox.showinfo(None, message='No. He was actually 6 feet 4.')
    if answer2 == "false":
        userscore = userscore + 1
    else:
        userscore = userscore - 1
    # Run the window's .mainloop() method
    answer3 = simpledialog.askstring(None, prompt='Are there true blue fireworks?')
    if answer3 == 'No':
        userscore = userscore + 1
        messagebox.showinfo(None, message="Yes, even though it's my favorite color.")
    else:
        userscore = userscore - 1
        messagebox.showinfo(None, message="You're wrong.")
    messagebox.showinfo(None, message="You're score is " + str(userscore))