file = open('input.txt', 'r')
f = file.readlines()

newList = []
for line in f:
    if line[-1] == '\n':
        newList.append(int(line[:-1]))
    else :
        newList.append(int(line))

#print(newList)

number_of_increases = 0
last_num = newList[0]


#part 1
#for x_num in newList:
#   if x_num > last_num :
#        number_of_increases += 1
#    last_num = x_num

#print(number_of_increases)

i = 0

part2_last_num = newList[0] + newList[1] + newList[2]
part2_num_of_increases = 0

#part 2
while i < len(newList)-2:
    part2_x_num = newList[i] + newList[i+1] + newList[i+2]
    if part2_x_num > part2_last_num:
        part2_num_of_increases += 1
    part2_last_num = part2_x_num
    i += 1

print(part2_num_of_increases)
