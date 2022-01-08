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

a = read_text("Input11.txt").splitlines()

row_count = len(a)
row_len = len(a[0])
flash_count = 0

class octopus:
    

    def __init__(self,level):
        self.level = level
        self.neighbours = []
        self.hasFlashed = False

    def run(self):

        global flash_count

        if self.hasFlashed == False:
            self.level += 1

            if self.level > 9:
                self.level = 0
                self.hasFlashed = True
                flash_count += 1
                for e in self.neighbours:
                    e.run()

grid = []

for row in a:
    new_row = []
    for element in row:
        new_row.append(octopus(int(element)))
    grid.append(new_row)

for rowIndex,row in enumerate(grid):
    for elementIndex,element in enumerate(row):
        if elementIndex != 0 :
            element.neighbours.append(grid[rowIndex][elementIndex-1])

            if rowIndex != 0 :
                element.neighbours.append(grid[rowIndex-1][elementIndex-1])

            if rowIndex != row_count-1:
                element.neighbours.append(grid[rowIndex+1][elementIndex-1])  

        if elementIndex != row_len-1:
            element.neighbours.append(grid[rowIndex][elementIndex+1]) 

            if rowIndex != 0 :
                element.neighbours.append(grid[rowIndex-1][elementIndex+1])

            if rowIndex != row_count-1:
                element.neighbours.append(grid[rowIndex+1][elementIndex+1])  

        if rowIndex != 0 :
            element.neighbours.append(grid[rowIndex-1][elementIndex])

        if rowIndex != row_count-1:
            element.neighbours.append(grid[rowIndex+1][elementIndex])  

for day in range(1000):

    start_flash_count = flash_count

    for row in grid:
        for element in row:
            element.run()

    for row in grid:
        for element in row:
            element.hasFlashed = False

    if flash_count == start_flash_count + (row_count*row_len):
        print(f"Days = {day+1}")


print(f"{flash_count}")
