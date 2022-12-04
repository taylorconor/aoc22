with open('04/input.txt') as f:
    lines = f.read().splitlines()

count = 0
for line in lines:
    x1, y1 = map(int, line.split(',')[0].split('-'))
    x2, y2 = map(int, line.split(',')[1].split('-'))
    count += max(x1, x2) <= min(y1, y2)

print("count = " + str(count))