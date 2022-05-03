from abc import ABC, abstractmethod
from platform import win32_edition
from tkinter import Tk, Frame, Button, X, Y, Toplevel, StringVar
from Game import Game, GameError
from itertools import product

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
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
        
        self.__root = root
    def __show_help(self):
        pass

    def __play_game(self):
        self.__game = Game()
        game_win = Toplevel(self.__root)
        game_win.title("Game")
        frame = Frame(game_win)
        frame.grid(row=0,column=0)

        self.__buttons = [[None for _ in range(3)] for _ in range(3)]
        for row,col in product(range(3),range(3)):
            b = StringVar()
            b.set(self.__game.at(row+1,col+1))
            self.__buttons[row][col] = b
            cmd = lambda r=row, c=col: self.__play(r,c)
            Button(
                frame, 
                textvariable = b,
                command = cmd
            ).grid(row=row,column=col)        

        Button(
            game_win,
            text = "Dismiss",
            command = game_win.destroy
        ).grid(row=1,column=0)

    def __play(self,r,c):
        self.__game.play(r+1,c+1)
        self.__buttons[r][c].set(self.__game.at(r+1,c+1))

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
