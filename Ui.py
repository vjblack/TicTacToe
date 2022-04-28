from abc import ABC, abstractmethod
from tkinter import Tk, Frame
from Game import Game, GameError

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
        self.__root = root

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
