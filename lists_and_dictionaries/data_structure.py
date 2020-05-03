# writing a tic-tac-toe game
import pprint
# create the playing board
theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
            "mid-L": " ", "mid-M": " ", "mid-R": " ",
            "low-L": " ", "low-M": " ", "low-R": " "}

# pprint.pprint(theBoard)

# Lets make the board more readable and display it like a proper tic-tac-toe game

def printBoard(board):
    print(board["top-L"] + "|" +
          board["top-M"] + "|" +
          board["top-R"])
    print("-----")
    print(board["mid-L"] + "|" +
          board["mid-M"] + "|" +
          board["mid-R"])
    print("-----")
    print(board["low-L"] + "|" +
          board["low-M"] + "|" +
          board["low-R"])

printBoard(theBoard)