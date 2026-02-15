def crear_matriz(rows, columns, numero):
    matriz = []
    print(f"\n--- Matriz {numero} ---")
    for i in range(rows):
        fila = []
        for j in range(columns):
            valor = int(input(f"Elemento [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz


def sumar_matrices(lista_matrices, rows, columns):
    resultado = []
    for i in range(rows):
        fila = []
        for j in range(columns):
            suma = sum(matriz[i][j] for matriz in lista_matrices)
            fila.append(suma)
        resultado.append(fila)
    return resultado


def imprimir_matrices(lista_matrices, resultado):
    print("\nResultado de la suma:\n")
    for i in range(len(resultado)):
        for matriz in lista_matrices:
            print(matriz[i], end="  +  ")
        print("=", resultado[i])
    print()


def main():
    cantidad = int(input("¿Cuántas matrices quieres sumar?: "))

    if cantidad < 2:
        print("Se necesitan dos o más matrices.")
        return

    rows = int(input("¿Cuántas filas?: "))
    columns = int(input("¿Cuántas columnas?: "))

    matrices = []

    for i in range(cantidad):
        matrices.append(crear_matriz(rows, columns, i + 1))

    resultado = sumar_matrices(matrices, rows, columns)
    imprimir_matrices(matrices, resultado)


if __name__ == "__main__":
    main()
