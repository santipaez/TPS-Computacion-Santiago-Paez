array = [1, 2, 10]
des_array = sorted (array, reverse=True)


def diferencia(des_array):
    b = []
    for i in range(len(des_array) - 1):
        b.append(des_array[i] - des_array[i + 1])
    print("Diferencia: ", b)

    def suma(b):
        suma = 0
        for numero in b:
            suma += numero
        return suma
    print("Sumatorio: ", suma(b))

print('Array: ', array)
print('Orden descendiente: ', des_array)
diferencia(des_array)
