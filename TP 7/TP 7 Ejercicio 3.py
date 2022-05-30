import random


def missing_no(list):
    list.sort()
    return [x for x in range(list[0], list[-1] + 1) if x not in list]

list = list(range(0, 101))
random.shuffle(list)
list.remove(5)
print(list)
missing_no(list)
print('El número que falta en la lista es:',missing_no(list))