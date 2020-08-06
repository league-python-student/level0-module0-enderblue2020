from tkinter import simpledialog, messagebox, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    answer = simpledialog.askstring(None, prompt='How old are you?')
    print('You are ' + answer + ' years old')