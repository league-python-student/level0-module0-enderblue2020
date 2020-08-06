from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    able = random.randint(0, 3)
    # 2. Print your variable to the console
    print(able)
    # 3. Get the user to enter something that they think is awesome
    simpledialog.askstring(None, prompt="Enter something that is awesome")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if able == 0:
        messagebox.showinfo(None, message="THAT. IS. AWESOME!")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if able == 1:
        messagebox.showinfo(None, message="It's ok, but it's not awesome")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if able == 2:
        messagebox.showinfo(None, message="That's BOOOOOOOOOOOOOOOOOOOOOOOOORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRIIIIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNGGGGGGGGGGGGGGGGGGGGG")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if able == 3:
        messagebox.showinfo(None, message="Fine. It's just fine")
    # Run the window's .mainloop() method
