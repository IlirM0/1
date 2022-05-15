data = open('input.txt', 'r')
data_array = data.readlines()

data_array = [(data_elem[:-1] if data_elem[-1] == '\n' else data_elem) for data_elem in data_array]
data_array = [data_element.split(" -> ") for data_element in data_array]
data_array = [[(data_elem[0].split(",")), (data_elem[1].split(","))] for data_elem in data_array]
data_array = [[[int(data_elem[0][0]),int(data_elem[0][1])],[int(data_elem[1][0]),int(data_elem[1][1])]]for data_elem in data_array]

class Vent:
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.is_line = False
        self.calc_is_line()

    def calc_is_line(self):
        if self.x1 == self.x2 or self.y1 == self.y2:
            self.is_line = True
        else:
            self.is_line = False

list_of_vents = []

max_x = 0
max_y = 0
for vent in data_array:
    list_of_vents.append(Vent(vent[0][0],vent[0][1],vent[1][0],vent[1][1]))
    if vent[0][0] > max_x:
        max_x = vent[0][0]
    if vent[1][0] > max_x:
        max_x = vent[0][0]
    if vent[0][1] > max_y:
        max_y = vent[0][0]
    if vent[1][1] > max_y:
        max_y = vent[0][0]

field = [[0 for i in range(max_x+1)] for j in range(max_y+1)]
# print(len(field))

def fill_field():
    for idx, single_vent in enumerate(list_of_vents):
        if single_vent.is_line:
            for x_range in range((single_vent.x1 if single_vent.x1 < single_vent.x2 else single_vent.x2), ((single_vent.x2 if single_vent.x1 < single_vent.x2 else single_vent.x1)+ 1)):
                for y_range in range((single_vent.y1 if single_vent.y1 < single_vent.y2 else single_vent.y2), ((single_vent.y2 if single_vent.y1 < single_vent.y2 else single_vent.y1)+ 1)):
                    field[x_range][y_range] = field[x_range][y_range] + 1
        else:
            x_range = single_vent.x1
            y_range = single_vent.y1
            while x_range <= single_vent.x2 if single_vent.x1 < single_vent.x2 else x_range >= single_vent.x2:
                field[x_range][y_range] = field[x_range][y_range] + 1
                if single_vent.x1 < single_vent.x2:
                    x_range = x_range + 1
                else:
                    x_range = x_range - 1
                if single_vent.y1 < single_vent.y2:
                    y_range = y_range + 1
                else:
                    y_range = y_range - 1
            # for x_range in range((single_vent.x1 if single_vent.x1 < single_vent.x2 else single_vent.x2), ((single_vent.x2 if single_vent.x1 < single_vent.x2 else single_vent.x1)+ 1)):
            #     field[x_range][y_range] = field[x_range][y_range] + 1
            #     if single_vent.y1 < single_vent.y2:
            #         y_range = y_range + 1
            #     else:
            #         y_range = y_range - 1
        # else:
        #     for x_range in range(single_vent.x1,(single_vent.x2+1)):
        #         for y_range in range(single_vent.y1,(single_vent.y2+1)):
        #             # print("index:",idx,"+ x , y:",x_range,",",y_range)
        #             field[x_range][y_range] = field[x_range][y_range] + 1

def calc_twos_in_field():
    all_twos = 0
    for i in field:
        for j in i:
            if j > 1:
                all_twos = all_twos + 1
    return all_twos

if __name__ == "__main__":
    pass
    fill_field()
    print("the twos in field:", calc_twos_in_field())
