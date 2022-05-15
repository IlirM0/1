import statistics

data = open('input.txt', 'r')
data_array = data.readlines()

data_array = data_array[0].split(",")

data_array = [int(data_elem) for data_elem in data_array]

unique_data_arr = []
for i in data_array:
    if i not in unique_data_arr:
        unique_data_arr.append(i)

# print(data_array)

median = int(statistics.median(data_array))

print(median)

total_fuel = 0

def tet_pyr(num):
    sums = 0
    while num != 0:
        sums = sums + num
        num = num - 1
    return sums

lowest_fuel = 107824779
for j in unique_data_arr:
    new_fuel = 0
    for i in data_array:
        new_fuel = new_fuel + tet_pyr(abs(j - i))
    if new_fuel < lowest_fuel:
        lowest_fuel = new_fuel




print(lowest_fuel)