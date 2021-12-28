from pathlib import Path
import pandas as pd


def read_text(name="input.txt"):
    directory = Path(__file__).parent
    text_file = directory / name
    return text_file.read_text()


a = read_text("Input2.txt").splitlines()

horiz = 0
vert = 0
aim = 0

for s in a:
    spt = s.split(" ")
    if spt[0] == "forward":
        horiz += int(spt[1])
        vert += int(spt[1]) * aim
    elif spt[0] == "up":
        aim -= int(spt[1])
    elif spt[0] == "down":
        aim += int(spt[1])
    else:
        raise RuntimeError("Ooops!")


print(horiz * vert)


if __name__ == "__main__":
    print("I was called")
