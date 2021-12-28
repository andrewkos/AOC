from pathlib import Path
import pandas as pd


def read_text(name="input.txt"):
    directory = Path(__file__).parent
    text_file = directory / name
    return text_file.read_text()


a = read_text("Input1.txt").splitlines()
b = [int(s) for s in a]

df = pd.DataFrame({"Main": b})
c = df["Main"].rolling(window=3).sum().values

counter = 0

for i, v in enumerate(c[1:]):
    if v > c[i]:
        counter += 1

print(counter)

if __name__ == "__main__":
    print("I was called")
