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


a = read_text("Input10.txt").splitlines()

class chunk():
    def __init__(self,message,parent):
        self.symbol = message[0]
        self.parent = parent
        