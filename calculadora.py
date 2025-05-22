class Matriz:
    def __init__(self, elementos):
        # asegura que la matriz tenga exactamente 2 filas y 2 columnas
        if len(elementos) != 2 or any(len(fila) != 2 for fila in elementos):
            raise ValueError("La matriz debe ser 2x2.")
        self.valores = elementos

    # método que se ejecuta al utilizar el operador de suma (+)
    def __add__(self, otra):
        return Matriz([
            [self.valores[0][0] + otra.valores[0][0], self.valores[0][1] + otra.valores[0][1]],
            [self.valores[1][0] + otra.valores[1][0], self.valores[1][1] + otra.valores[1][1]]
        ])

    # método que se ejecuta al utilizar el operador de resta (-)
    def __sub__(self, otra):
        return Matriz([
            [self.valores[0][0] - otra.valores[0][0], self.valores[0][1] - otra.valores[0][1]],
            [self.valores[1][0] - otra.valores[1][0], self.valores[1][1] - otra.valores[1][1]]
        ])

    # método que se ejecuta al utilizar el operador de multiplicación (*)
    def __mul__(self, otra):
        a = self.valores
        b = otra.valores
        return Matriz([
            [
                a[0][0]*b[0][0] + a[0][1]*b[1][0],
                a[0][0]*b[0][1] + a[0][1]*b[1][1]
            ],
            [
                a[1][0]*b[0][0] + a[1][1]*b[1][0],
                a[1][0]*b[0][1] + a[1][1]*b[1][1]
            ]
        ])

    def __str__(self):
        return f"|{self.valores[0][0]}  {self.valores[0][1]}|\n|{self.valores[1][0]}  {self.valores[1][1]}|"

# solicita al usuario los valores para construir una matriz 2x2
def leer_matriz(numero):
    print(f"> Matriz {numero}:")
    matriz = []
    for i in range(2):
        fila = []
        for j in range(2):
            valor = int(input(f"> Matriz {numero}: elemento {i},{j}\n< "))
            fila.append(valor)
        matriz.append(fila)
    return Matriz(matriz)

# punto de entrada principal del programa
def main():
    m1 = leer_matriz(1)
    m2 = leer_matriz(2)

    # se muestran las matrices introducidas por el usuario
    print("> Matriz 1:")
    print(m1)
    print("> Matriz 2:")
    print(m2)

    print("> Escriba 1 para suma,")
    print(">         2 para resta,")
    print(">         3 para multiplicación")
    opcion = input("< ")

    if opcion == "1":
        resultado = m1 + m2
        print("> La suma de las dos matrices es:")
        print(resultado)
    elif opcion == "2":
        resultado = m1 - m2
        print("> La resta de las dos matrices es:")
        print(resultado)
    elif opcion == "3":
        resultado = m1 * m2
        print("> La multiplicación de las dos matrices es:")
        print(resultado)
    else:
        print("> Opción no válida.")

if __name__ == "__main__":
    main()
