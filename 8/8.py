data = open('input.txt', 'r')
data_array = data.readlines()

data_array = [(data_elem[:-1] if data_elem[-1] == '\n' else data_elem) for data_elem in data_array]
data_array = [data_element.split(" ") for data_element in data_array]

print(data_array)


# total = 0
# for i in data_array:
#     for j in range(1,5):
#         if len(i[-j]) == 2 or len(i[-j]) == 3 or len(i[-j]) == 4 or len(i[-j]) == 7:
#             total = total +1
# print(total)

## testing
# total = 0
# for i in data_array:
#     has_2_len = False
#     has_3_len = False
#     has_4_len = False
#     has_7_len = False
#     for j in range(0,10):
#         if len(i[j]) == 2:
#             has_2_len = True
#         if len(i[j]) == 3:
#             has_3_len = True
#         if len(i[j]) == 4:
#             has_4_len = True
#         if len(i[j]) == 7:
#             has_7_len = True
#         print(len(i[j]), end=' ')
#     print("| has 2:",has_2_len,"has 3:", has_3_len, "has 4:",has_4_len,"has7:",has_7_len)

class Segment:
    def __init__(self, string):
        self.length = len(string)
        self.characters = sorted(string)
        if self.length == 2:
            self.number = "1"
        elif self.length == 3:
            self.number = "7"
        elif self.length == 4:
            self.number = "4"
        elif self.length == 7:
            self.number = "8"
        else:
            self.number = "-"

class Line:
    def __init__(self):
        self.first = []
        self.final = []


    def print_line(self):
        for i in self.first:
            print(i.number, end=" ")
        print("|",end=" ")
        for i in self.final:
            print(i.number, end=" ")
        print(" ")

lines_array = []

# total = 0
for i in data_array:
    temp = Line()
    for j in range(10):
        temp.first.append(Segment(i[j]))
    for j in range(11,15):
        temp.final.append(Segment(i[j]))
    lines_array.append(temp)

for i in lines_array:
    i.print_line()