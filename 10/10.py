data = open('temp_input.txt', 'r')
data_array = data.readlines()

data_array = [(data_elem[:-1] if data_elem[-1] == '\n' else data_elem) for data_elem in data_array]

def map_func(n):
    if n == '(' or n == '[' or n == '{' or n == '<':
        return [n,'open', 'status']
    else:
        return [n, 'close', 'status']

data_array = [list( map(map_func,i) ) for i in data_array]

print(data_array)