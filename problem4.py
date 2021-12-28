from pathlib import Path
from typing import List
import pandas as pd


def read_text(name="input.txt"):
    directory = Path(__file__).parent
    text_file = directory / name
    return text_file.read_text()

a = read_text("Input4.txt").splitlines()

# ------------------ Get bingo calls ---------------------------

calls = a[0].split(',')

# ------------------ Get board raw data ------------------------
boardBlockIndex = -1
rowIndex = 0
boardBlocks = []

for i in range(1,len(a)):
    if a[i] == "":
         boardBlocks.append([])
         boardBlockIndex += 1
    else:
        boardBlocks[boardBlockIndex].append(a[i])
# --------------------------------------------------------------

class Board:
    def __init__(self,boardBlock:List[str]):
            self.numbers = [someStr.split() for someStr in boardBlock]

            self.observed = [[False for _ in range(5)] for _ in range(5)]

            self.hasWon = False

    def observe(self,call:str):
            for rowIndex,row in enumerate(self.numbers):
                for elementIndex,element in enumerate(row):
                    if element == call:
                        self.observed[rowIndex][elementIndex] = True

    def score(self,lastObserved:str):
            totalScore = 0
            for rowIndex,row in enumerate(self.observed):
                for elementIndex,wasObserved in enumerate(row):
                    if not(wasObserved):
                        totalScore += int(self.numbers[rowIndex][elementIndex])

            return totalScore*int(lastObserved)

    def bingo(self):

            for rowTest in range(5):
                    if self.observed[rowTest][0] == True and self.observed[rowTest][1] == True and self.observed[rowTest][2] == True and self.observed[rowTest][3] == True and self.observed[rowTest][4] == True: 
                            self.hasWon = True

            for colTest in range(5):
                    if self.observed[0][colTest] == True and self.observed[1][colTest] == True and self.observed[2][colTest] == True and self.observed[3][colTest] == True and self.observed[4][colTest] == True: 
                            self.hasWon = True

            return self.hasWon

            
boards = [Board(bb) for bb in boardBlocks]


for c in calls:
    for b in boards:
        if b.hasWon == False:
            b.observe(c)
            if b.bingo():
                finished = True
                print(b.score(c))
         


#print(f"{boardBlocks}")

if __name__ == "__main__":
    print("I was called")
