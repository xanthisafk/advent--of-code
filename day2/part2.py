with open('input.txt', 'r') as f:
    data = f.readlines()

horizontal, depth, aim = 0, 0, 0

for i in range(len(data)):
    line = data[i].split(' ')
    if line[0] == 'down':
        aim += int(line[1])
    elif line[0] == 'up':
        aim -= int(line[1])
    else:
        depth += aim * int(line[1])
        horizontal += int(line[1])

print(f'Horizontal: {horizontal}\nAim: {aim}\nDepth: {depth}\nAnswer: {horizontal*depth}')
