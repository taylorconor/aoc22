with open('06/input.txt') as f:
    line = f.read().strip()

window = list(line[:4])
for i in range(4, len(line)):
    if len(set(window)) == 4:
        break
    window.pop(0)
    window.append(line[i])

print("i = " + str(i))