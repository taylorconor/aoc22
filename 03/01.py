with open('03/input.txt') as f:
    lines = f.read().splitlines()

prio = 0
for line in lines:
    common = set(line[:len(line)//2]).intersection(set(line[len(line)//2:])).pop()
    prio += ord(common.swapcase()) - (70 if common.isupper() else 64)

print("prio = " + str(prio))