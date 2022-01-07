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

scores_2 = {")": 1,
            "]": 2,
            "}": 3,
            ">": 4}

a = read_text("Input10.txt").splitlines()

class chunk():
    def __init__(self):
        self.open_symbol = None
        self.close_symbol = None
        self.parent = None
        self.is_corrupt = False
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

        if score != 0:
            self.is_corrupt = True

        return score

    def autocomplete(self):
        if self.close_symbol is None:
            return pairs[self.open_symbol]
        else:
            return ""

    def autocomplete_self_and_children(self):

        output = ""

        for child in self.children:
                   output += child.autocomplete_self_and_children()
        
        output += self.autocomplete()

        return output


score = 0
score_2_autocompletes = []

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
    if start_chunk.is_corrupt == False:
        score_2_autocompletes.append(start_chunk.autocomplete_self_and_children())

def score_strings(s:str):
    score = 0
    for e in s:
        lookup = scores_2[e]    
        score = score*5 + lookup
        print(f"{e},{lookup},{score}")
        
    return score

scores_2_results = [score_strings(s) for s in score_2_autocompletes]


test = score_strings("])}>")

print(f"test = {test}")

#print(f"{score_2_autocompletes}")        
#print(f"{scores_2_results}")        

scores_2_sorted = scores_2_results.copy()
scores_2_sorted.sort()


print(f"{scores_2_sorted}")        
print(f"{scores_2_sorted[len(scores_2_sorted)//2]}")