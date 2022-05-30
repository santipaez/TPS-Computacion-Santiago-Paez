import random


def juego():
    if all(elem in sorteo for elem in bingo):
        print('¡WIN!')
        return True
    else:
        print("PERDIÓ. No pudo formar la palabra BINGO")
        return False

sorteo=[random.randint(1, 26) for x in range(10)]
bingo=[2, 4, 7, 9, 14, 15]
print(sorteo)
comparacion = [item for item in sorteo if item in bingo]

print(juego())
