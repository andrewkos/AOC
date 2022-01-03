from pathlib import Path
import re
from typing import List
import time
#import pandas as pd
import timeit
import sys

def read_text(name="input.txt"):
    directory = Path(__file__).parent
    text_file = directory / name
    return text_file.read_text()


a = read_text("Input9.txt").splitlines()

grid = []

for row in a:
    newRow = []
    for element in row:
        newRow.append(int(element))
    grid.append(newRow)


height = len(grid)
width = len(grid[0])

print(f"{grid}")