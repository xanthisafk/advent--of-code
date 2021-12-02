with open('input.txt', 'r') as f:
    data = f.readlines()

horizontal, depth = 0, 0

for i in range(len(data)):
    line = data[i].split(' ')
    if line[0] == 'forward':
        horizontal += int(line[1])
    elif line[0] == 'up':
        depth -= int(line[1])
    else:
        depth += int(line[1])

print(f'Horizontal: {horizontal}\nDepth: {depth}\nAnswer: {horizontal*depth}')
