with open('08/input.txt') as f:
    lines = [list(map(int, x)) for x in f.read().splitlines()]

def score(r, c):
    product = 1
    for d in [reversed(lines[r][:c]), lines[r][c+1:], reversed([x[c] for x in lines[:r]]), [x[c] for x in lines[r+1:]]]:
        sum = 0
        for n in d:
            sum += 1
            if n >= lines[r][c]:
                break
        product *= max(1, sum)
    return product

max_score = max(score(r, c) for r in range(len(lines)) for c in range(len(lines[r])))

print("max_score = " + str(max_score))
