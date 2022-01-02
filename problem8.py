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


a = read_text("Input8.txt").splitlines()
b = [s.split("|") for s in a]
c = [[s[0].split(),s[1].split()] for s in b]

#a : 8
#b : 6
#c : 8
#d : 7
#e : 4
#f : 9
#g : 7

# If count=7 and In "4"? then its d
# If count=8 and in "1"? then its c

