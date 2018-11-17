import numpy as np
import os


def alt_matrix_generator(matrix_in):
    """
    Genera la matriz alterna a matrix_in
    :param matrix_in: numpy array, matriz de entrada para generar la nueva matriz.
    :return: numpy array.
    """
    matrix_out = np.zeros((np.size(matrix_in, 0), np.size(matrix_in, 1)))
    print("Matriz de tamaño", np.size(matrix_in, 0), "x", np.size(matrix_in, 1))
    for i in range(0, np.size(matrix_in, 0)):
        for j in range(0, np.size(matrix_in, 1)):
            if j-1 > 0:
                matrix_out[i][j] = float(matrix_in[i][j]) - float(matrix_in[i][j-1])  # Asignación del nuevo valor
            else:
                matrix_out[i][j] = float(matrix_in[i][j]) - float(matrix_in[i][0])  # Asignación para j-1 =< 0
        print(matrix_out)
    return matrix_out


def matrix_file_reader(filename):
    matrix = None
    matrix_values_list = []     # Almacena los valores hasta que se conoce el tamaño de la matriz de entrada
    columns = 0
    rows = 0

    if os.path.isfile(filename):
        with open(filename, 'r', newline='\n') as file:
            for line in file:
                rows = rows + 1  # Cuenta las filas
                line_array = line.split()
                matrix_values_list = matrix_values_list + line_array
                if columns == 0:
                    columns = len(line_array)  # Reconoce las columnas
        matrix = np.asarray(matrix_values_list)
        matrix = np.reshape(matrix, (rows, columns))
    return matrix


def main():
    filename = "input.txt"
    foo = matrix_file_reader(filename)
    print("Entrada:\n", foo, "\n")
    if foo is not None:
        print("\n", alt_matrix_generator(foo))


if __name__ == '__main__':
    main()
