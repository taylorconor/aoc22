with open('06/input.txt') as f:
    line = f.read().strip()

window = list(line[:14])
for i in range(14, len(line)):
    if len(set(window)) == 14:
        break
    window.pop(0)
    window.append(line[i])

print("i = " + str(i))