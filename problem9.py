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


a = read_text("Input9.txt").splitlines()

grid = []
is_low_point = []
mapped = []

for row in a:
    newRow = []
    mappedRow = []
    for element in row:
        newRow.append(int(element))
        mappedRow.append(True if int(element) == 9 else False)
    grid.append(newRow)
    mapped.append(mappedRow)

height = len(grid)
width = len(grid[0])
result = 0



class basinNode():
    def __init__(self,rowIndex,elementIndex):
            self.children = []
            print(f"new node = {rowIndex}, {elementIndex} = {grid[rowIndex][elementIndex]}")
            mapped[rowIndex][elementIndex] = True
            if elementIndex!=0:
                if element < grid[rowIndex][elementIndex-1]:
                    if mapped[rowIndex][elementIndex-1] == False: 
                        self.children.append(basinNode(rowIndex,elementIndex-1))


            if elementIndex!=width-1:
                if (element < grid[rowIndex][elementIndex+1]):
                    if mapped[rowIndex][elementIndex+1] == False: 
                        self.children.append(basinNode(rowIndex,elementIndex+1))

            if rowIndex!=0:
                 if (element < grid[rowIndex-1][elementIndex]):
                     if mapped[rowIndex-1][elementIndex] == False: 
                         self.children.append(basinNode(rowIndex-1,elementIndex))

            if rowIndex!=height-1:
                 if (element < grid[rowIndex+1][elementIndex]):
                     if mapped[rowIndex+1][elementIndex] == False: 
                         self.children.append(basinNode(rowIndex+1,elementIndex))

    def basinSize(self):
            count = 0
            if len(self.children) > 0:
                    count += len(self.children)
                    for child in self.children:
                        bs = child.basinSize()
                        count += bs

            return count

basinsizes = []

for rowIndex,row in enumerate(grid):
    newRow = []
    for elementIndex,element in enumerate(row):
        leftTest = True if elementIndex==0 else (element < grid[rowIndex][elementIndex-1])
        rightTest = True if elementIndex==width-1 else (element < grid[rowIndex][elementIndex+1])
        upTest = True if rowIndex==0 else (element < grid[rowIndex-1][elementIndex])
        downTest = True if rowIndex==height-1 else (element < grid[rowIndex+1][elementIndex])
        testResult = leftTest and rightTest and upTest and downTest
        newRow.append(testResult)
        if testResult:
                print(f"Found Basin at {rowIndex},{elementIndex}")
                basin = basinNode(rowIndex,elementIndex)
                basinsizes.append(basin.basinSize())
                result += element +1

    is_low_point.append(newRow)

basinsizes.sort(reverse=True)

print(f"{basinsizes}")
print(f"{(basinsizes[0]+1)*(basinsizes[1]+1)*(basinsizes[2]+1)}")
print(f"{result}")