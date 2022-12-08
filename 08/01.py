with open('08/input.txt') as f:
    lines = [list(map(int, x)) for x in f.read().splitlines()]

def is_visible(r, c):
    return any(all(x < lines[r][c] for x in y) for y in
               [lines[r][:c], lines[r][c+1:], [x[c] for x in lines[:r]], [x[c] for x in lines[r+1:]]])

visible = sum(is_visible(r, c) for r in range(len(lines)) for c in range(len(lines[r])))
print("visible = " + str(visible))
