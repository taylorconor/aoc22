with open('02/input.txt') as f:
    lines = [x.strip() for x in f.read().splitlines()]

score = 0
for line in lines:
    opponent = 1 + ord(line[0]) - ord('A')
    response = 1 + ord(line[2]) - ord('X')
    score += response
    if opponent == response:
        score += 3
    if (response == 1 and opponent == 3) or (response == 2 and opponent == 1) or (response == 3 and opponent == 2):
        score += 6

print("score = " + str(score))