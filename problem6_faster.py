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

state_a = [0,0,0,0,0,0,0,0,0]
state_b = [0,0,0,0,0,0,0,0,0]
range_a = [0,1,2,3,4,5,6,7,8]

for s in a:
    state_a[int(s)] += 1

def count_fish():
    count= sum(state_a)
    print(f"{count}")    

def evolve_state(remainingDays:int):

    if remainingDays != 0:

        for key in range_a:
            fishCount = state_a[key]
            if key == 0:
                state_b[8]=fishCount
                state_b[6]=fishCount
            elif key==7:
                state_b[key-1] += fishCount
            else:
                state_b[key-1]=fishCount

        for key in range_a:
            fishCount = state_b[key]
            if key == 0:
                state_a[8]=fishCount
                state_a[6]=fishCount
            elif key==7:
                state_a[key-1] += fishCount
            else:
                state_a[key-1] = fishCount                


        #count_fish()
        evolve_state(remainingDays-1)


result = timeit.timeit(lambda:evolve_state(128),number=1 )

#result = evolve_state(128)
print(f"{result}")
count_fish()

