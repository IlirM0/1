# open de data
data = open('input.txt', 'r')
# split de data na elke \n
data_array = data.readlines()
# haal elke \n weg van een lijn code
data_array = [(data_elem[:-1] if data_elem[-1] == '\n' else data_elem) for data_elem in data_array]
# split de lijn na elke -
data_array = [data_elem.split("-") for data_elem in data_array]

# data_array[x][0] = waar path begint, data_array[x][1] waar path eindigd
print(data_array)

list_of_caves = []

static_double_visit_available = True
class Cave:
    def __init__(self, name):
        self.name = name
        self.isBig = name.isupper()
        self.isStart = True if name == 'start' else False
        self.isEnd = True if name == 'end' else False
        self.canVisit = True
        self.canDoubleVisit = True
        self.neighbours = []
        # self.visits = 0


class Path:
    def __init__(self, line):
        self.begin = Cave(line[0])
        self.end = Cave(line[1])


def init_caves():
    global list_of_caves
    list_of_caves = []
    for i in data_array:
        for j in i:
            if not is_in_cave_array(j):
                list_of_caves.append(Cave(j))
    add_neighbours()


def is_in_cave_array(name):
    for i in list_of_caves:
        if i.name == name:
            return True
    return False


def add_neighbours():
    for d in data_array:
        for i in range(len(list_of_caves)):
            if d[0] == list_of_caves[i].name:
                for j in range(len(list_of_caves)):
                    if d[1] == list_of_caves[j].name:
                        list_of_caves[i].neighbours.append(list_of_caves[j])
            elif d[1] == list_of_caves[i].name:
                for j in range(len(list_of_caves)):
                    if d[0] == list_of_caves[j].name:
                        list_of_caves[i].neighbours.append(list_of_caves[j])


number_of_routes = 0
def path_find():
    for st in list_of_caves:
        if st.isStart:
            # print("id =",hex(id(st)))
            # st.canVisit = False
            find_end(st)
    # print(number_of_routes)


def find_end(cave):
    global static_double_visit_available
    if cave.canVisit:
        if not cave.isBig:
            cave.canVisit = False
        if not cave.isEnd:
            for neighbours in cave.neighbours:
                find_end(neighbours)
        else:
            global number_of_routes
            number_of_routes = number_of_routes + 1
        cave.canVisit = True
    elif static_double_visit_available and not cave.isStart:
        static_double_visit_available = False
        for neighbours in cave.neighbours:
            find_end(neighbours)
        static_double_visit_available = True



def reset_caves():
    for o in list_of_caves:
        o.canVisit = True


# def reset_list():
# #     for i in range(len(path_array)):
# #         path_array[i].begin.canVisit = True
# #         path_array[i].end.canVisit = True


if __name__ == "__main__":
    init_caves()
    # for i in list_of_caves:
    #     print(i.name, hex(id(i)))
    #     for j in i.neighbours:
    #         print("-",j.name, hex(id(j)))
    path_find()
    print(number_of_routes)
    # print(path_array[0].begin.isEnd)
