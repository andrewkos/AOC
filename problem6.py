from pathlib import Path
import re
from typing import List
import time
#import pandas as pd
import timeit



VENT_RE = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

def read_text(name="input.txt"):
    directory = Path(__file__).parent
    text_file = directory / name
    return text_file.read_text()

a = read_text("Input6.txt").split(",")

state = {0 : 0,
         1 : 0,
         2 : 0,
         3 : 0,
         4 : 0,
         5 : 0,
         6 : 0,
         7 : 0,
         8 : 0}

for s in a:
    key = int(s)
    state[key] = state[key]+1

def count_fish():
    count= 0 

    for key in state.keys():
        count += state[key]

    print(f"{count}")    

def evolve_state(remainingDays:int):
    global state
    if remainingDays != 0:
        newState = {}

        for key in state.keys():
            fishCount = state[key]
            if key == 0:
                newState[8]=fishCount
                if newState.__contains__(6):
                    newState[6]= newState[6] + fishCount
                else:
                    newState[6]=fishCount
            else:
                if newState.__contains__(key-1):
                    newState[key-1]= newState[key-1] + fishCount
                else:
                    newState[key-1]=fishCount

        state = newState
        #count_fish()
        evolve_state(remainingDays-1)


result = timeit.timeit(lambda:evolve_state(256),number=1 )
#result = evolve_state(256)
print(f"{result}")
count_fish()

