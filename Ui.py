from abc import ABC, abstractmethod
from platform import win32_edition
from tkinter import Tk, Frame, Button, X, Y, Toplevel, StringVar, Scrollbar, Text, LEFT, RIGHT, Grid, N,S,E,W, END
from Game import Game, GameError
from itertools import product

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        self.__game_win = None
        root = Tk()
        root.title("Tic Tac Toe")
        frame = Frame(root)
        frame.pack()
        Button(
            frame,
            text = "Help",
            command = self.__show_help
         ).pack(fill=X)

        Button(
            frame,
            text = "Play",
            command = self.__play_game
         ).pack(fill=X)

        Button(
            frame,
            text = "Quit",
            command = self.__quit
         ).pack(fill=X)
         
        scroll = Scrollbar(frame)
        console = Text(frame, height=4, width=50)
        scroll.pack(side=RIGHT, fill=Y)
        console.pack(side=LEFT, fill=Y)

        scroll.config(command=console.yview)
        console.config(yscrollcommand=scroll.set)
        
        self.__root = root
        self.__console = console #save the console for adding text later
    def __show_help(self):
        pass

    def __play_game(self):
        #if the game window already exists, pressing the play button should have no effect
        if self.__game_win:
            return

        self.__finished = False
        self.__game = Game()
        game_win = Toplevel(self.__root)
        game_win.title("Game")
        frame = Frame(game_win)
        frame.grid(row=0,column=0)

        #to allow resizing
        Grid.columnconfigure(game_win, 0, weight=1)
        Grid.rowconfigure(game_win, 0, weight=1)
        frame.grid(row=0, column=0, sticky=N+S+E+W)


        self.__buttons = [[None for _ in range(3)] for _ in range(3)]
        for row,col in product(range(3),range(3)):
            b = StringVar()
            b.set(self.__game.at(row+1,col+1))
            self.__buttons[row][col] = b
            cmd = lambda r=row, c=col: self.__play(r,c) #anonymous funciton with default arguments
            Button(
                frame, 
                textvariable = b,
                command = cmd #calls command with no arguments, uses default and allows value to be played
            ).grid(row=row,column=col, sticky=N+S+E+W)        

        for i in range(3):
            Grid.rowconfigure(frame, i, weight=1)
            Grid.columnconfigure(frame, i, weight=1)

        self.__game_win = game_win

        Button(
            game_win,
            text = "Dismiss",
            command = self.__dismiss_game_win
        ).grid(row=1,column=0)
        

    def __dismiss_game_win(self):
        self.__game_win.destroy()
        self.__game_win = None

    def __play(self,r,c):
        #if the game is finished pressing a button in the frame should have no effect
        if self.__finished:
            return
        try:
            self.__game.play(r+1,c+1)
        except GameError as e:
            self.__console.insert(END, f"{e}\n")
        self.__buttons[r][c].set(self.__game.at(r+1,c+1))
        if self.__game.winner == Game.DRAW:
            self.__console.insert(END, "Game is drawn\n")
            self.__finished = True
        elif self.__game.winner:
            self.__console.insert(END,f"Game is won by {self.__game.winner}\n")
            self.__finished = True  

    def __quit(self):
        self.__root.quit()

    def run(self):
        self.__root.mainloop()

class Terminal(Ui):
    def __init__(self):
        self.__game = Game()

    def __get_input(self):
        while True:
            try:
                #type check
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
                #range check
                if 1 <= row <= 3 and 1 <= col <= 3:
                    break
                else:
                    print("Invalid input, please try again")
                break
            except ValueError:
                print("Invalid input, please try again")
        return row,col

    def run(self):
        while self.__game.winner == None:
            print(self.__game)
            row, col = self.__get_input()
            try:
                self.__game.play(row, col)
            except GameError as e:
                print(e)
        print(self.__game)
        if self.__game.winner == Game.DRAW:
            print("The game was drawn")
        print(f"The winner is {self.__game.winner}")
