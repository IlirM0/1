data = open('input.txt', 'r')
data_array = data.readlines()

data_array = [(data_elem[:-1] if data_elem[-1] == '\n' else data_elem) for data_elem in data_array]

height = len(data_array)
width = len(data_array[0])

data_array = [list(data_elem) for data_elem in data_array]

def map_func(n):
    return [int(n),'-']

data_array = [list( map(map_func,i) ) for i in data_array]
# data_array = [list( map(int,i) ) for i in data_array]

num_of_basins = 0

def recursive_investation(x,y):
    for i in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0 <= y+i[0] < height and 0 <= x + i[1] < width and data_array[y + i[0]][x + i[1]][0] != 9 and data_array[y + i[0]][x + i[1]][1] == '-':
            data_array[y + i[0]][x + i[1]][1] = num_of_basins
            recursive_investation(x+i[1], y+i[0])


# # data_array[HEIGHT][WIDTH][INFO]
# # INFO 0 = the number
# # INFO 1 = the basin number
# zeroes = 0
# calc_total_danger = 0
for h in range(height):
    for w in range(width):
        # for i in [[1,0],[-1,0],[0,1],[0,-1]]:
        #     if 0 <= h+i[0] < height and 0 <= w + i[1] < height:
        if data_array[h][w][1] == '-' and data_array[h][w][0] != 9:
            recursive_investation(w, h)
            num_of_basins = num_of_basins + 1

arr_of_basins = [0] * num_of_basins

for h in range(height):
    for w in range(width):
        # for i in [[1,0],[-1,0],[0,1],[0,-1]]:
        #     if 0 <= h+i[0] < height and 0 <= w + i[1] < height:
        if data_array[h][w][0] != 9:
            arr_of_basins[data_array[h][w][1]] = arr_of_basins[data_array[h][w][1]] + 1

arr_of_basins.sort()

print("value =", arr_of_basins[-1]*arr_of_basins[-2]*arr_of_basins[-3])

#         if data_array[h][w] == 0:
#             print(data_array[h][w], "in x:", w + 1, ", y:", h + 1)
#         if is_smallest:
#             # if data_array[h][w] == 0:
#             #     zeroes = zeroes + 1
#             # print(data_array[h][w], "in x:", w + 1, ", y:", h + 1)
#             # print(data_array[h][w], end="")
#             calc_total_danger = calc_total_danger + data_array[h][w] + 1
# print(" ")
# print("zeroes:",zeroes)
# print(calc_total_danger)
#
# print("h",height)
# print("w",width)

# print(arr_of_basins)

# 1786