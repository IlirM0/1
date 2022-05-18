data = open('input.txt', 'r')
data_array = data.readlines()
data_array = [(data_elem[:-1] if data_elem[-1] == '\n' else data_elem) for data_elem in data_array]
height = len(data_array)
width = len(data_array[0])
total_flashes = 0


def map_func(n):
    return [int(n), 'no flash']


data_array = [list(map(map_func, i)) for i in data_array]


def reset_flash():
    for h in range(height):
        for w in range(width):
            data_array[h][w][1] = 'no flash'


def flash(h, w):
    global total_flashes
    for i in [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]:
        if 0 <= h + i[0] < height and 0 <= w + i[1] < width:
            if data_array[h + i[0]][w + i[1]][1] == 'no flash' and data_array[h + i[0]][w + i[1]][0] == 9:
                data_array[h + i[0]][w + i[1]][0] = 0
                data_array[h + i[0]][w + i[1]][1] = 'flash'
                total_flashes = total_flashes + 1
                flash(h + i[0], w + i[1])
            elif data_array[h + i[0]][w + i[1]][1] == 'no flash' and data_array[h + i[0]][w + i[1]][0] != 9:
                data_array[h + i[0]][w + i[1]][0] = data_array[h + i[0]][w + i[1]][0] + 1


def init():
    global total_flashes
    for h in range(height):
        for w in range(width):
            if data_array[h][w][0] == 9 and data_array[h][w][1] == 'no flash':
                data_array[h][w][0] = 0
                data_array[h][w][1] = 'flash'
                total_flashes = total_flashes + 1
                flash(h, w)
            elif data_array[h][w][1] == 'no flash':
                data_array[h][w][0] = data_array[h][w][0] + 1


def all_flash():
    for h in range(height):
        for w in range(width):
            if data_array[h][w][1] == 'no flash':
                return False
    return True


period = 1000
for i in range(period):
    init()
    if i == period-1:
        for j in data_array:
            print(j)
    if all_flash():
        print("all flash at step:", i+1)
    reset_flash()

print("total flashes:", total_flashes)
