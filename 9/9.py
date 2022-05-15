data = open('input.txt', 'r')
data_array = data.readlines()

data_array = [(data_elem[:-1] if data_elem[-1] == '\n' else data_elem) for data_elem in data_array]

height = len(data_array)
width = len(data_array[0])

data_array = [list(data_elem) for data_elem in data_array]

data_array = [list( map(int,i) ) for i in data_array]

# data_array[HEIGHT][WIDTH]
zeroes = 0
calc_total_danger = 0
for h in range(height):
    for w in range(width):
        is_smallest = True
        for i in [[1,0],[-1,0],[0,1],[0,-1]]:
            try:
                if h+i[0] >= 0 and w+i[1] >= 0 :
                    if data_array[h+i[0]][w+i[1]] <= data_array[h][w]:
                        is_smallest = False
            except:
                pass
        if data_array[h][w] == 0:
            print(data_array[h][w], "in x:", w + 1, ", y:", h + 1)
        if is_smallest:
            # if data_array[h][w] == 0:
            #     zeroes = zeroes + 1
            # print(data_array[h][w], "in x:", w + 1, ", y:", h + 1)
            # print(data_array[h][w], end="")
            calc_total_danger = calc_total_danger + data_array[h][w] + 1
print(" ")
print("zeroes:",zeroes)
print(calc_total_danger)

print("h",height)
print("w",width)

print(data_array)

# 1786