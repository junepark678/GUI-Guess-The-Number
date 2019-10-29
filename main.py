#guess the number game
import random
from tkinter import *
from tkinter import messagebox

score = 0

tk = Tk()
L2Text = StringVar(master=tk)
L1Text = StringVar(master=tk)
# what happens when submit button is clicked
def submit(*args, **kwargs):
    global playerGuess, score
    score = score+1
    playerGuess = E1.get()
    playerGuess = int(playerGuess)
    if playerGuess==numToGuess:
        L1Text.set("you won!")
        messagebox.showinfo("Score", f"Your score was {score}")
        playAgain = messagebox.askyesno("play again?", "Do you want to play again?")
        if playAgain:
            start()
        else:
            tk.destroy()

    elif playerGuess>numToGuess:
        L2Text.set("Guess lower")

    else:
        L2Text.set("Guess Higher")



# defines starting variables
def start():
    global numToGuess, playerGuess, L1Text, L2Text
    numToGuess = random.randint(1, 100)
    playerGuess = 0

    L1Text.set("Guess a number between 1 and 100")
    L2Text.set("Make a guess")




start()
# defines main widgets
tk.title("guess the number")
L1 = Label(tk, textvariable=L1Text)
L1Text.set("Guess a number between 1 and 100")
L1.pack()
L2 = Label(tk, textvariable=L2Text)
L2Text.set("Make a guess")
L2.pack()
E1 = Entry(tk)
E1.pack()
B1 = Button(tk, text="Submit", command=submit)
B1.pack()
# binding the return/enter key to run submit functions
tk.bind("<Return>", submit)

mainloop()
