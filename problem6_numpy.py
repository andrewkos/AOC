from pathlib import Path
import re
from typing import List
import time
#import pandas as pd
import timeit
import numpy as np
from numpy.linalg import matrix_power


VENT_RE = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

def read_text(name="input.txt"):
    directory = Path(__file__).parent
    text_file = directory / name
    return text_file.read_text()

a = read_text("Input6.txt").split(",")

state = [0,0,0,0,0,0,0,0,0]

A = np.array([[0,1,0,0,0,0,0,0,0],
              [0,0,1,0,0,0,0,0,0],
              [0,0,0,1,0,0,0,0,0],
              [0,0,0,0,1,0,0,0,0],
              [0,0,0,0,0,1,0,0,0],
              [0,0,0,0,0,0,1,0,0],
              [1,0,0,0,0,0,0,1,0],
              [0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0]])

for s in a:
    state[int(s)] += 1.0

state_vector = state = np.array(state).transpose()

def count_fish():
    count= np.sum(state_vector)
    print(f"{count}") 

def evolve_state(remainingDays:int):
        global state_vector
        state_vector = matrix_power(A,remainingDays)*state_vector
        #print(f"{state_vector}")
        #print(f"{matrix_power(A,remainingDays)}")

result = timeit.timeit(lambda:evolve_state(256),number=1 )

#result = evolve_state(128)
print(f"{result}")
count_fish()

