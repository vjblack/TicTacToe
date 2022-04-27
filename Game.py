
class Game:

    EMPTY = " "
    P1 = "o"
    P2 = "x"
    def __init__(self):
        self.__board = [[Game.EMPTY for _ in range(3)] for _ in range(3)]
        self.__player = Game.P1

    def __repr__(self):
        return "Look! It's the 'board'!"

    def play(self,row,col):
        row -= 1 #zero-base the row and column
        col -= 1
        self.__board[row][col] = self.__player
        if self.__player == Game.P1:
            self.__player = Game.P2
        else:
            self.__player = Game.P1
    
    @property
    def winner(self):
        return None
#hello, can you see this change???
if __name__ == "__main__":
    pass
