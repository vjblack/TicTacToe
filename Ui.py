from abc import ABC, abstractmethod
from Game import Game

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        self.__game = Game()

    def __get_input(self):
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        return row,col

    def run(self):
        while self.__game.winner == None:
            print(self.__game)
            row, col = self.__get_input()
            self.__game.play(row, col)
        print(f"The winner is {self.__game.winner}")
