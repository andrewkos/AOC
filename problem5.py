from pathlib import Path
import re
from typing import List
import pandas as pd

VENT_RE = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

def read_text(name="input.txt"):
    directory = Path(__file__).parent
    text_file = directory / name
    return text_file.read_text()

a = read_text("Input5.txt").splitlines()
coords = [[int(e) for e in re.search(VENT_RE, s).groups()] for s in a]

maxx = 0
maxy = 0

for myTuple in coords:
    if myTuple[0]>maxx:
        maxx = myTuple[0]
    if myTuple[1]>maxy:
        maxy = myTuple[1]
    if myTuple[2]>maxx:
        maxx = myTuple[2]
    if myTuple[3]>maxy:
        maxy = myTuple[3]

print(f"MaxX= {maxx}")
print(f"MaxY= {maxy}")

grid = [[0 for ycoord in range(maxy+1)] for xcoord in range(maxx+1)]

print(f"{grid}")

