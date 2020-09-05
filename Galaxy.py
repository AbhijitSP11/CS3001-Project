from tkinter import *
from PIL import ImageTk, Image
#main window 
main_win = Tk()

#size of the window
main_win.geometry("1800x960")

#background image
bg = PhotoImage(file="lost_in_space.png")
PhotoImage = Label(image= bg,bg = "black",height = 1000,width = 1800).place(x = 0,y = 0)

#Title of the Game
Label(main_win, text = 'GALAXY',fg = "black", bg="red", font =("orbitron", 100)).place(x = 520,y = 200)

#defining message for buttons
def inst():
    messagebox.showinfo("Help", "Follow the instructions,
                        The game starts from “Start” at bottom left and end at “Got the crystal” The game can be played with one or more than one player, 
                        ➢ The player can move by rolling the dice, 
                        ➢ The player has to move according the number on the dice, 
                        ➢ After the first player rolls the dice, second should get the chance to roll the dice and move his token, 
                        ➢ The game has special cards with some tasks written, when a player lands on a tile without a number on a special tile, 
                        The card asks to accomplish a task, if the player accepts the task he can move. If he does not accept the card, he should 10 steps back,
                        ➢ The player wins the game if the token lands on the last tile with text")
    
#Creating a new window
def playgame():
    global game_bg
    game_wn = Toplevel()
    game_wn.geometry("1800x960")
    game_wn.title("Galaxy")
    game_bg = ImageTk.PhotoImage(Image.open("board game-Recovered (1).png"))
    my_label = Label(game_wn,image = game_bg).pack()


    
#creating buttons
button1 = Button(main_win, text = "Play Game",command = playgame, fg = "white", bg = "orange", 
                 padx = 50, pady = 5,font =("orbitron", 15)).place(x = 800, y = 480)
button2 = Button(main_win, text = "Instructions",command = inst,fg = "white", bg = "orange", 
                 padx = 42, pady = 5, font =("orbitron", 15)).place(x = 800, y = 580)
button3 = Button(main_win, text = "Exit Game",command = main_win.destroy, fg = "white", bg = "orange",
                 padx = 55, pady = 5, font =("orbitron", 15)).place(x = 800, y = 680)

#main event loop fro screen
main_win.mainloop()
