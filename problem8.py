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

# 0 : 6
# 1 : 2
# 2 : 5
# 3 : 5
# 4 : 4
# 5 : 5
# 6 : 6
# 7 : 3
# 8 : 7
# 9 : 6

finalResult = 0

for sA in c:

    mapping = {}

    def identify_one(patterns):
        for p in patterns:
            if len(p) == 2:
                signalSet = set()
                for p_x in p:
                    signalSet.add(p_x)
                mapping[1]=signalSet

    def identify_four(patterns):
        for p in patterns:
            if len(p) == 4:
                signalSet = set()
                for p_x in p:
                    signalSet.add(p_x)
                mapping[4]=signalSet

    def identify_seven(patterns):
        for p in patterns:
            if len(p) == 3:
                signalSet = set()
                for p_x in p:
                    signalSet.add(p_x)
                mapping[7]=signalSet

    def identify_eight(patterns):
        for p in patterns:
            if len(p) == 7:
                signalSet = set()
                for p_x in p:
                    signalSet.add(p_x)
                mapping[8]=signalSet


    def signalcontains(signal,number):
            contains = True

            signalSet = set()
            for p_x in signal:
                signalSet.add(p_x)

            number_pattern = mapping[number]
            for p in number_pattern:
                contains = contains and signalSet.__contains__(p)

            return contains


    def identify_zero_six_nine(patterns):
        for p in patterns:
            if len(p) == 6:

                signalSet = set()
                for p_x in p:
                    signalSet.add(p_x)

                if signalcontains(p,4):
                    mapping[9]=signalSet
                elif signalcontains(p,1):
                    mapping[0]=signalSet
                else:
                    mapping[6]=signalSet

    def identify_two_three_five(patterns):
        for p in patterns:
            if len(p) == 5:

                signalSet = set()
                for p_x in p:
                    signalSet.add(p_x)

                if signalcontains(p,1):
                    mapping[3]=signalSet
                elif len(signalSet - mapping[4]) == 3:
                    mapping[2]=signalSet
                else:
                    mapping[5]=signalSet

    def decode(pattern):
            signalSet = set()
            for p_x in pattern:
                signalSet.add(p_x)

            result = -1

            for key in mapping.keys():
                if mapping[key]==signalSet:
                    result = key

            return result

    identify_one(sA[0])
    identify_four(sA[0])
    identify_seven(sA[0])
    identify_eight(sA[0])
    identify_zero_six_nine(sA[0])
    identify_two_three_five(sA[0])

    finalResult += decode(sA[1][0])*1000
    finalResult += decode(sA[1][1])*100
    finalResult += decode(sA[1][2])*10
    finalResult += decode(sA[1][3])


print(f"{finalResult}")
#a : 8
#b : 6
#c : 8
#d : 7
#e : 4
#f : 9
#g : 7

# If count=7 and In "4"? then its d
# If count=8 and in "1"? then its c

