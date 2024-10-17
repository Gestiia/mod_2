import random

def number_1():
    number = list(range(3, 21))
    random_ = random.choice(number)
    return random_

def number_2(n):
    pass_ = {}
    pass_.update({3: 12})
    pass_.update({4: 13})
    pass_.update({5: 1423})
    pass_.update({6: 121524})
    pass_.update({7: 162534})
    pass_.update({8: 13172635})
    pass_.update({9: 1218273645})
    pass_.update({10: 141923283746})
    pass_.update({11: 11029384756})
    pass_.update({12: 12131511124210394857})
    pass_.update({13: 112211310495867})
    pass_.update({14: 1611325212343114105968})
    pass_.update({15: 1214114232133124115106978})
    pass_.update({16: 1317115262143531341251161079})
    pass_.update({17: 11621531441351261171089})
    pass_.update({18: 12151811724272163631545414513612711810})
    pass_.update({19: 118217316415514613712811910})
    pass_.update({20: 13141911923282183731746416515614713812911})
    passcode = pass_.get(n)
    return passcode


m = number_1()

combo_1 = list(range(1, m))
combo_2 = list(range(1, m))
pairs = []
result = ''

for i in combo_1:
    for j in combo_2:
        c1 = i
        c2 = j
        if c1 >= c2:
            continue
        else:
            c3 = m % (c1 + c2)
            if c3 == 0:
                pairs.append([c1, c2])
                result = result + str(c1) + str(c2)
print('Первое число: ', m)
print('Второе число: ', result)


