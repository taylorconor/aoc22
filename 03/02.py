with open('03/input.txt') as f:
    lines = f.read().splitlines()

prio = 0
for i in range(0, len(lines), 3):
    common = set(lines[i]).intersection(set(lines[i+1]).intersection(set(lines[i+2]))).pop()
    prio += ord(common.swapcase()) - (70 if common.isupper() else 64)

print("prio = " + str(prio))