with open('04/input.txt') as f:
    lines = f.read().splitlines()

count = 0
for line in lines:
    x1, y1 = map(int, line.split(',')[0].split('-'))
    x2, y2 = map(int, line.split(',')[1].split('-'))
    count += (x1 >= x2 and y1 <= y2) or (x2 >= x1 and y2 <= y1)

print("count = " + str(count))