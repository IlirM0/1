file = open('input.txt', 'r')
f = file.readlines()

distance = 0
depth = 0
aim = 0

i = 0
while i < len(f):
    if f[i].split()[0] == 'forward':
        distance += int(f[i].split()[1])
        depth += (aim * int(f[i].split()[1]))
    elif f[i].split()[0] == 'up':
        aim -= int(f[i].split()[1])
    elif f[i].split()[0] == 'down':
        aim += int(f[i].split()[1])
    i += 1

print(distance*depth)
