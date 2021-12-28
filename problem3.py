from pathlib import Path
import pandas as pd


def read_text(name="input.txt"):
    directory = Path(__file__).parent
    text_file = directory / name
    return text_file.read_text()


a = read_text("Input3.txt").splitlines()



oxygenfiltered = a.copy()
i=0

while len(oxygenfiltered) > 1 :
    
    counts = [[0, 0] for j in range(0, 12)]

    for s in oxygenfiltered:
        for j, e in enumerate(s):
            if e == "0":
                counts[j][0] += 1
            elif e == "1":
                counts[j][1] += 1
            else:
                raise RuntimeError("Fuck!")

    mostCommon = "0"    
    if counts[i][1] >= counts[i][0]:
        mostCommon = "1"

    #print(f"Most common ({i}) = {mostCommon}")

    oxygenfiltered = list(filter(lambda mystr : mystr[i] == mostCommon,oxygenfiltered))
    #print(f"Oxygen candidates = {len(oxygenfiltered)}")
    i += 1

co2filtered = a.copy()
i=0

while len(co2filtered) > 1 :

    counts = [[0, 0] for j in range(0, 12)]

    for s in co2filtered:
        for j, e in enumerate(s):
            if e == "0":
                counts[j][0] += 1
            elif e == "1":
                counts[j][1] += 1
            else:
                raise RuntimeError("Fuck!")


    leastCommon = "0"    
    if counts[i][1] < counts[i][0]:
        leastCommon = "1"

    #print(f"Least common ({i}) = {leastCommon}")

    co2filtered = list(filter(lambda mystr : mystr[i] == leastCommon,co2filtered))
    #print(f"Co2 candidates = {len(co2filtered)}")
    i += 1

oxygenstring = oxygenfiltered[0]
co2string = co2filtered[0]

print(f"Oxygen Candidate = {oxygenstring}")
print(f"CO2 Candidate = {co2string}")

oxygenNumber = 0
co2Number = 0

for i in range(0,12):
    oxygenNumber += int(oxygenstring[i]) * (2 ** (11 - i))
    co2Number += (int(co2string[i])) * (2 ** (11 - i))

print(oxygenNumber*co2Number)

# gamma = []
#for A in counts:
#    if A[0] > A[1]:
#        gamma.append(0)
#    else:
#        gamma.append(1)

#gammaNum = 0
#epsilonNum = 0

#for i, g in enumerate(gamma):
#    gammaNum += g * (2 ** (11 - i))
#    epsilonNum += (1 - g) * (2 ** (11 - i))

#print(gammaNum * epsilonNum)

if __name__ == "__main__":
    print("I was called")
