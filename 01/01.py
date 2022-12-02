with open('01/input.txt') as f:
    lines = [x.strip() for x in f.read().splitlines()]

max_calories = running_total = 0
for line in lines:
    if len(line) == 0:
        if running_total > max_calories:
            max_calories = running_total
        running_total = 0
    else:
        running_total += int(line)

print("max calories: " + str(max_calories))