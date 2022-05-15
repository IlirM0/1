data = open('input.txt', 'r')
data_array = data.readlines()

data_array = data_array[0].split(",")

data_array = [int(data_elem) for data_elem in data_array]

complete_data = [0 for i in range(9)]
# print(complete_data)

for i in data_array:
    complete_data[i] = complete_data[i] + 1

print(complete_data)

# for days in range(18):
#     for i in range(len(data_array)):
#         if data_array[i] != 0:
#             data_array[i] = data_array[i] - 1
#         else:
#             data_array[i] = 6
#             data_array.append(8)
#     # print(data_array)
#
# print(len(data_array))

def calc_total():
    sums = 0
    for i in range(len(complete_data)):
        sums = sums + complete_data[i]
    return sums

for days in range(256):
    new_eights = complete_data[0]
    for i in range(1,9):
        complete_data[i-1] = complete_data[i]
    complete_data[8] = new_eights
    complete_data[6] = complete_data[6] + new_eights
    # print(complete_data)

print(calc_total())