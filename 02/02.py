with open('02/input.txt') as f:
    lines = [x.strip() for x in f.read().splitlines()]

score = 0
for line in lines:
    opponent = 1 + ord(line[0]) - ord('A')
    if line[2] == 'X':
        response = 3 if opponent == 1 else response
        response = 1 if opponent == 2 else response
        response = 2 if opponent == 3 else response
    if line[2] == 'Y':
        response = opponent
        score += 3
    if line[2] == 'Z':
        response = 1 if opponent == 3 else response
        response = 2 if opponent == 1 else response
        response = 3 if opponent == 2 else response
        score += 6
    score += response

print("score = " + str(score))