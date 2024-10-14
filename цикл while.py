my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

condition = 0

while condition < len(my_list):

    if my_list[condition] < 0:
        break

    if my_list[condition] > 0:
        print(my_list[condition])

    condition += 1
