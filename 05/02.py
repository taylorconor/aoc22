with open('05/input.txt') as f:
    lines = f.read().splitlines()

stacks = [[] for x in range(9)]
for i in range(len(lines)):
    if lines[i][1] == '1':
        i += 2
        break
    for j in range(9):
        if lines[i][j*4] != ' ':
            stacks[j].insert(0, lines[i][j*4+1])

for i in range(i, len(lines)):
    nums = [int(s) for s in lines[i].split() if s.isdigit()]
    stacks[nums[2]-1].extend(stacks[nums[1]-1][-nums[0]:])
    stacks[nums[1]-1] = stacks[nums[1]-1][:len(stacks[nums[1]-1]) - nums[0]]

result = ""
for stack in stacks:
    result += stack[len(stack)-1]
print("result = " + result)