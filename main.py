from tkinter import*
import random
 #creating user interface
guiWindow=Tk()
guiWindow.title("The Rock Paper Scissor")
guiWindow.configure(background="skyblue")

#adding label to the window
heading = Label(
    guiWindow,
    text='Let\'s play Rock Paper Scissor',
    font='arial 18 bold',
    bg='#588C7E',
    fg='white',
).pack()
userinput=StringVar()

subHeading=Label(
    guiWindow,
    text='Select any ONE from rock,paper,scissor',
    font='calibri 16 bold',
    bg='#ff7200'
).place(
    x=35,
    y=110
)

Entry(
    guiWindow,
    font='calibri 14',
    textvariable=userinput,
    bg='#FBEFCC'
).place(
    x=110,
    y=160
)
#scores
userscore=Label(
    guiWindow,
    text=0,
    font=100,
    bg="#9b59b6",
    fg="white"
)
computerscore=Label(
    guiWindow,
    text=0,
    font=100,
    bg="#9b59b6",
    fg="white"
)
computerscore=random.randint(1,1)
userscore=random.randint(1,3)
# code for computer selection
compSelection=random.randint(1,3)

if compSelection == 1:
    compSelection='rock'
elif compSelection==2:
    compSelection='paper'
else:
    compSelection='scissors'

#creating function to begin the game
res = StringVar()

def letsPlay():
    userSelection=userinput.get()
    if userSelection==compSelection:
        res.set("its a Tie!You made a same choice as computer.")
    elif userSelection == 'rock' and compSelection=='paper':
        res.set("Oops! You Lose. Computer selected paper.")
    elif userSelection == 'rock' and compSelection == 'scissors':
        res.set("Congrats! You Win. Computer selected Scissors.")
    elif userSelection == 'paper' and compSelection == 'scissors':
        res.set("Oops! You Lose. Computer selected Scissors.")
    elif userSelection == 'paper' and compSelection == 'rock':
        res.set("Congrats ! You Win. Computer selected Rock.")
    elif userSelection == 'scissors' and compSelection == 'rock':
        res.set("Oops! You Lose. Computer selected Rock.")
    elif userSelection == 'scissors' and compSelection == 'paper':
        res.set("Congrats! You Win. Computer selected Paper.")
    else:
        res.set("Look like an invalid input!Consider selecting from- rock,pape & scissors")

# defining a function to reset the game
def resetGame():
    res.set("")
    userinput.set("")

#defining a function to exit the game
def exitGame():
    guiWindow.destroy()

displayResult=Label(
    guiWindow,
    textvariable=res,
    font='calibri 12 bold',
    bg='#96CEB4',

).place(
    x=20,
    y=240
)
playButton=Button(
    guiWindow,
    font='arial 12 bold',
    text='PLAY',
    padx=9,
    bg='#96CEB4',
    command =letsPlay
).place(
    x=100,
    y=300
)
reseButton = Button(
    guiWindow,
    font='arial 12 bold',
    text='RESET',
    padx=10,
    bg='#96CEB4',
    command=resetGame
).place(
    x=200,
    y=300
)
exitButton = Button(
    guiWindow,
    font='aria 12 bold',
    text='EXIT',
    padx=10,
    bg='#96CEB4',
    command=exitGame
).place(
    x=300,
    y=300
)
guiWindow.mainloop()









