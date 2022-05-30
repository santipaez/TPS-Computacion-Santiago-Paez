# Ejercicio 7. Escribir un programa, que dado un archivo de texto, un delimitador,
# y una lista de campos, imprima solamente esos campos, separados por ese delimitador.

class read_txt_file:
    def __init__(self, text, separator):
        self.text = text
        self.separator = separator
    def read_text(self):
        self.separator = input("Ingresa el separador que quieras utilizar: ")
        f = open(self.text, "r")
        lineas = f.readlines()
        string = ' '.join(lineas)
        lista = string.split(" ")
        string2 = self.separator.join(lista)
        print(string2)

texto = read_txt_file("C:\\Users\\Usr\\PycharmProjects\\SEGUNDO AÑO\\TP 3\\ejercicio7.txt", " ")
print(texto.read_text())