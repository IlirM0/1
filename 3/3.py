data = open('input.txt', 'r')
data_array = data.readlines()

# take out the '\n' 's from the data array
sorted_data_array = []
for data_line in data_array :
    if data_line[-1] == '\n':
        sorted_data_array.append(data_line[:-1])
    else :
        sorted_data_array.append(data_line)

binary_sorted_data_array = [0 for i in range(len(sorted_data_array))]

#make the data actually binary
for j in range(len(sorted_data_array)):
    for i in range(12):
        if sorted_data_array[j][i] == '1':
            binary_sorted_data_array[j] += (1<<(11-i))


#part 1
#initialize array with 12 elements all containing a 0
counted_ones_in_data = [0 for i in range(12)]

#count the ones
for i in range(len(binary_sorted_data_array)): # loop through every binary number in data list
    for j in range(12) :                # loop through every single number of a binary number
        if (binary_sorted_data_array[i] & (1 << j) )> 0 :
            counted_ones_in_data[j] += 1


gamma = 0
epsilon = 0

for i in range(12):
    if counted_ones_in_data[i] > 500 : #if there are more than 500 counted ones, then its a binary 1
        gamma += (1<<(i))
    else : # i cannot do epsilon = ~gamma, because it will also invert signed bit
        epsilon += (1<<(i))

#print(f'output part 1: {epsilon*gamma}')


#part 2
#oxy_data_array = [[]*12 for i in range(12)] #create an array of 12 arrays

oxy_data_array = []
for i in range(len(binary_sorted_data_array)):
    oxy_data_array.append(binary_sorted_data_array[i])
# print(oxy_data_array)
new_oxy_data_array = []
oxy_count_ones = 0
#print(oxy_data_array)
#print(oxy_data_array)

exit_ = False

#print(1 << (11))
while not exit_:
    for i in range(12):
        #print(oxy_data_array)
        for oxy_num in oxy_data_array:
            if (oxy_num & (1 << (11-i))) > 0:
                oxy_count_ones += 1
        #print(oxy_count_ones)
        if oxy_count_ones >= (len(oxy_data_array)/2):
            for oxy_num in oxy_data_array:
                if (oxy_num & (1 << (11 - i))) > 0:
                    new_oxy_data_array.append(oxy_num)
        else:
            for oxy_num in oxy_data_array:
                if (oxy_num & (1 << (11 - i))) == 0:
                    new_oxy_data_array.append(oxy_num)
        oxy_data_array.clear()
        for k in range(len(new_oxy_data_array)):
            oxy_data_array.append(new_oxy_data_array[k])
        new_oxy_data_array.clear()
        oxy_count_ones = 0
        if len(oxy_data_array) == 1:
            exit_ = True
print(f'final oxygen generator rating: {oxy_data_array}')

co2_data_array = []
for i in range(len(binary_sorted_data_array)):
    co2_data_array.append(binary_sorted_data_array[i])
# print(co2_data_array)
new_co2_data_array = []
co2_count_zeroes = 0

exit_ = False

# ENTER THE BELOW PORTION WITH CAUTION. PROCEED WITH EYE BLEACH IF NECESSARY

while not exit_:
    for i in range(12):
        for co2_num in co2_data_array:
            if (co2_num & (1 << (11-i))) == 0:
                print(co2_num)
                co2_count_zeroes += 1
        print(f'counted zeroes: {co2_count_zeroes}')
        if len(co2_data_array) == 1:
            exit_ = True
        if not exit_:
            if co2_count_zeroes <= (len(co2_data_array) / 2):
                for co2_num in co2_data_array:
                    if (co2_num & (1 << (11 - i))) == 0:
                        new_co2_data_array.append(co2_num)
            else:
                for co2_num in co2_data_array:
                    if (co2_num & (1 << (11 - i))) > 0:
                        new_co2_data_array.append(co2_num)
            co2_data_array.clear()
            for k in range(len(new_co2_data_array)):
                co2_data_array.append(new_co2_data_array[k])
            new_co2_data_array.clear()
            co2_count_zeroes = 0
            print(f'len(co2_data_array): {len(co2_data_array)}')
            print('=========================')

print(f'final co2 generator rating: {co2_data_array}')

print(f'final awns: {co2_data_array[0] * oxy_data_array[0]}')
