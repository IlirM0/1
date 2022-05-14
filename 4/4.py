data = open('input.txt', 'r')
data_array = data.readlines()

numbs = data_array.pop(0)
data_array.pop(0)

numbs = numbs.split(",")

# data_array = [(False if data_elem == '\n' else data_elem) for data_elem in data_array]
data_array = [(data_elem[:-1] if data_elem[-1] == '\n' else data_elem) for data_elem in data_array]

data_array = [data_element.split(" ") for data_element in data_array]

numbs = [int(num_element) for num_element in numbs]

print(data_array)
print(numbs)


class Ticket:
    def __init__(self, name):
        self.numbers = []
        self.name = name
        self.round_it_won = 0
        self.win = False

    def has_won(self, roundL):
        if not self.win:
            for vertical in range(5):
                if (self.numbers[0+vertical] == True and self.numbers[5+vertical] == True and self.numbers[10+vertical] == True and self.numbers[15+vertical] == True and self.numbers[20+vertical] == True) or (self.numbers[0+(vertical*5)] == True and self.numbers[1+(vertical*5)] == True and self.numbers[2+(vertical*5)] == True and self.numbers[3+(vertical*5)] == True and self.numbers[4+(vertical*5)] == True):
                    self.win = True
                    self.round_it_won = roundL

def last_win_num(l_winning_num):
    if every_ticket_won():
        index_of_l_w = highest_won_ticket_num()
        total_remaining_num = 0
        for p in tickets[index_of_l_w].numbers:
            if p is not True:
                total_remaining_num = total_remaining_num + p
        print("Number:", l_winning_num * total_remaining_num)

tickets = [Ticket(0)]

number_of_ticket = 0

for lis in data_array:
    # print(lis)
    if lis != ['']:
        for i in lis:
            if i != '':
                tickets[number_of_ticket].numbers.append(int(i))
    else:
        number_of_ticket = number_of_ticket + 1
        tickets.append(Ticket(number_of_ticket))
del number_of_ticket

def remove_num(number):
    for i in range(len(tickets)):
        for j in range(len(tickets[i].numbers)):
            if tickets[i].numbers[j] == number:
                tickets[i].numbers[j] = True

def every_ticket_won():
    for i in tickets:
        if not i.win:
            return False
    return True

def highest_won_ticket_num():
    l_w_round = 0
    l_w_num = 0
    for i in tickets:
        if i.round_it_won > l_w_round:
            l_w_round = i.round_it_won
            l_w_num = i.name
    return l_w_num

for idx, nummer in enumerate(numbs):
    remove_num(nummer)
    for nu in range(len(tickets)):
        tickets[nu].has_won(idx)
    last_win_num(nummer)
#     print()

