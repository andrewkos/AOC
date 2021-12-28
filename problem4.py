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

class board:
    def __init__(self,boardBlock:List[str]):
            self.numbers = [for someStr in boardBlock :
                                 spl = str.split(" ")
                                 list(filter(lambda someStr: someStr != "",spl))]



print(f"{boardBlocks}")

if __name__ == "__main__":
    print("I was called")
