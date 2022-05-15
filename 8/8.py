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

def compare_two_arrays(arr1, arr2):
    number_of_same = 0
    for i in arr1.characters:
        for j in arr2.characters:
            if i == j:
                number_of_same = number_of_same +1
    return number_of_same

def exact_two_arrays(arr1, arr2):
    number_of_same = 0
    for i in arr1.characters:
        for j in arr2.characters:
            if i == j:
                number_of_same = number_of_same +1
    if number_of_same == len(arr1.characters) and number_of_same == len(arr2.characters):
        return True
    else:
        return False

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
        self.final_num = 0


    def print_line(self):
        for i in self.first:
            print(i.number, end=" ")
        print("|",end=" ")
        for i in self.final:
            print(i.number, end=" ")
        print("| number:", self.final_num, end=" ")
        print("")

    def fix_all_first(self):
        for i in range(10):
            if self.first[i].number == "-" and self.first[i].length == 5:
                if compare_two_arrays(self.first[i], self.return_from_name("1")) == 2:
                    self.first[i].number = "3"
                elif compare_two_arrays(self.first[i], self.return_from_name("4")) == 3:
                    self.first[i].number = "5"
                else:
                    self.first[i].number = "2"
            elif self.first[i].number == "-" and self.first[i].length == 6:
                if compare_two_arrays(self.first[i], self.return_from_name("4")) == 4:
                    self.first[i].number = "9"
                elif compare_two_arrays(self.first[i], self.return_from_name("7")) == 3:
                    self.first[i].number = "0"
                else:
                    self.first[i].number = "6"

    def fix_all_final(self):
        for i in range(4):
            if self.final[i].number == "-":
                for j in range(10):
                    if exact_two_arrays(self.final[i],self.first[j]):
                        self.final[i].number = self.first[j].number

    def fix_all(self):
        self.fix_all_first()
        self.fix_all_final()
        temp_final_num = [i.number for i in self.final]
        self.final_num = int("".join(temp_final_num))

    def return_from_name(self, name):
        for i in self.first:
            if i.number == name:
                return i
        return False

lines_array = []

# total = 0
for i in data_array:
    temp = Line()
    for j in range(10):
        temp.first.append(Segment(i[j]))
    for j in range(11,15):
        temp.final.append(Segment(i[j]))
    temp.fix_all()
    lines_array.append(temp)

summed_num = 0
for i in lines_array:
    summed_num = summed_num + i.final_num
    i.print_line()
print("summed num:", summed_num)

def sort_line(list):
    sorted_line = []
