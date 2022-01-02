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


a = read_text("Input7.txt").split(",")

state = {}

for s in a:
    i = int(s)
    if state.__contains__(i):
        state[i]=state[i]+1
    else:
        state[i]=1

max_location = max(state.keys())
locations = [i for i in range(max_location+1)]

fuel_costs = {0:0,
              1:1}

for l in locations[2::]:
    fuel_costs[l] = fuel_costs[l-1]+l



minDistance = 999999999999999

for endpointKey in locations:
    dist = 0
    for startpointKey in state.keys():
            dist += fuel_costs[abs(endpointKey-startpointKey)]*state[startpointKey]

    if dist < minDistance:
        minDistance = dist

print(f"{minDistance}")