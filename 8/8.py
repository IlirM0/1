data = open('input.txt', 'r')
data_array = data.readlines()

data_array = [(data_elem[:-1] if data_elem[-1] == '\n' else data_elem) for data_elem in data_array]
data_array = [data_element.split(" ") for data_element in data_array]

print(data_array)

total = 0
for i in data_array:
    for j in range(1,5):
        if len(i[-j]) == 2 or len(i[-j]) == 3 or len(i[-j]) == 4 or len(i[-j]) == 7:
            total = total +1

print(total)