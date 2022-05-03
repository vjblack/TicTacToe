from itertools import product
class GameError(Exception):
    pass
class Game:

    EMPTY = " "
    P1 = "o"
    P2 = "x"
    DRAW = "draw"
    def __init__(self):
        self.__board = [[Game.EMPTY for _ in range(3)] for _ in range(3)]
        self.__player = Game.P1

    def __repr__(self):
        result = "  " + " ".join(str(i+1) for i in range(3))
        for row in range(3):
            result += f"\n{row+1} " + "|".join(self.__board[row])
            if row != 2:
                dashes = "-" * 5
                result += f"\n  {dashes}"
        result += f"\n\n{self.__player} turn to play"
        return result

    def at(self,row,col):
        row -=1
        col -=1 #zero base
        return self.__board[row][col]

    def play(self,row,col):
        row -= 1 #zero-base the row and column
        col -= 1
        if self.__board[row][col] != Game.EMPTY:
            raise GameError("Cannot play here!")
        self.__board[row][col] = self.__player
        if self.__player == Game.P1:
            self.__player = Game.P2
        else:
            self.__player = Game.P1
    
    @property
    def winner(self):
        for p in (Game.P1, Game.P2):
            for row in range(3): #checks all rows
                if all(self.__board[row][col] == p for col in range(3)):
                    return p
            for col in range(3): #checks all columns
                if all(self.__board[row][col] == p for row in range(3)):
                    return p
            if all(self.__board[2-i][i] == p for i in range(3)):
                return p
            if not any(self.__board[row][col] == Game.EMPTY for row, col in product(range(3), range(3))):
                return Game.DRAW
        return None
#hello, can you see this change???
if __name__ == "__main__":
    pass
