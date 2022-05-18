data = open('input.txt', 'r')
data_array = data.readlines()

data_array = [(data_elem[:-1] if data_elem[-1] == '\n' else data_elem) for data_elem in data_array]

def map_func(n):
    if n == '(' or n == '[' or n == '{' or n == '<':
        return [n,'open', 'good']
    else:
        return [n, 'close', 'status']

data_array = [list( map(map_func,i) ) for i in data_array]

part_2_points = []

for line in data_array:
    queue = []
    skip = False
    for character in line:
        if character[1] == 'open':
            queue.append(character)
        else:
            temp = queue.pop()
            if temp[0] == '(' and character[0] == ')' or temp[0] == '[' and character[0] == ']' or temp[0] == '<' and character[0] == '>' or temp[0] == '{' and character[0] == '}':
                character[2] = 'good'
            else:
                character[2] = 'corrupted'
                skip = True
    # print("queue")
    # print(queue)
    if not skip:
        queue.reverse()
        line_points = 0
        for incomplete in queue:
            line_points = line_points * 5
            if incomplete[0] == '(':
                line_points = line_points + 1
            elif incomplete[0] == '[':
                line_points = line_points + 2
            elif incomplete[0] == '{':
                line_points = line_points + 3
            elif incomplete[0] == '<':
                line_points = line_points + 4
        part_2_points.append(line_points)

# points = 0
# for line in data_array:
#     for character in line:
#         if character[2] == 'corrupted':
#             if character[0] == ')':
#                 points = points + 3
#             elif character[0] == ']':
#                 points = points + 57
#             elif character[0] == '}':
#                 points = points + 1197
#             elif character[0] == '>':
#                 points = points + 25137
#             break

part_2_points = sorted(part_2_points)

middle = int((len(part_2_points)-1)/2)

print(part_2_points[middle])

# print(part_2_points)
# print(data_array)