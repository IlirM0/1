data = open('input.txt', 'r')
data_array = data.readlines()

data_array = data_array[0].split(",")

data_array = [int(data_elem) for data_elem in data_array]

print(data_array)