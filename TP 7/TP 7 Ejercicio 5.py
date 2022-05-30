
def consecutive(a, b):
    for i in list:
        if a == list[i] and b == list[i+1] or a == list[i] and b == list[i-1]:
            return True
        else:
            return False

list = [1, 3, 5, 7]
a = list[1]
b = list[2]
consecutive(a, b)
print(consecutive(a, b))