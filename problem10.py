from pathlib import Path
import re
from typing import List
import time
#import pandas as pd
import timeit
import sys

sys.setrecursionlimit(1000)

def read_text(name="input.txt"):
    directory = Path(__file__).parent
    text_file = directory / name
    return text_file.read_text()


pairs = {"(" : ")",
         "<" : ">",
         "[" : "]",
         "{" : "}"}

scores = {")": 3,
          "]": 57,
          "}": 1197,
          ">": 25137}

a = read_text("Input10.txt").splitlines()

class chunk():
    def __init__(self):
        self.open_symbol = None
        self.close_symbol = None
        self.parent = None
        self.children = []

    def check(self):
        score = 0
        #print(f"Check {self.open_symbol}{self.close_symbol}")
        if (self.close_symbol != pairs[self.open_symbol]):
            if not(self.close_symbol is None):
                 #print(f"Mismatch {self.open_symbol}{self.close_symbol}")
                 score += scores[self.close_symbol]

        return score

    def check_self_and_children(self):
        score = self.check()
        if len(self.children) > 0:
            for child in self.children:
                if score == 0:
                        #print("here")
                        score += child.check_self_and_children()

        return score

score = 0

for str in a:

    start_chunk = chunk()
    start_chunk.open_symbol = str[0]
    #print(f"{start_chunk.open_symbol}")
    working_chunk = start_chunk
    for element in str[1::]:
        if pairs.keys().__contains__(element):
            new_chunk = chunk()
            new_chunk.open_symbol = element
            #print(f"New chunk = {new_chunk.open_symbol}")
            new_chunk.parent = working_chunk
            working_chunk.children.append(new_chunk)
            working_chunk = new_chunk
        else:
            working_chunk.close_symbol = element
            #print(f"Close chunk = {new_chunk.close_symbol}")
            #print(f"{working_chunk.open_symbol}{working_chunk.close_symbol}")
            working_chunk = working_chunk.parent
            

    score += start_chunk.check_self_and_children()

print(f"{score}")

        