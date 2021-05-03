from time import sleep as slp
count = 0
with open("lyrics.txt") as f:
    lines = f.readlines()
    for line in lines:
        count += 1
        print(line.strip())
        slp(0.1)
