import numpy as np
import os


def alt_matrix_generator(matrix_in):
    """
    Genera la matriz alterna a matrix_in
    :param matrix_in: numpy array, matriz de entrada para generar la nueva matriz.
    :return: numpy array.
    """
    matrix_out = np.zeros((np.size(matrix_in, 0), np.size(matrix_in, 1)+1))   # Genera un ndarray de 0's
    print("Matriz de tamaño", np.size(matrix_in, 0), "x", np.size(matrix_in, 1)+1)
    for i in range(0, np.size(matrix_in, 0)):
        for j in range(0, np.size(matrix_in, 1)+1):
            try:
                if j == 0:
                    matrix_out[i][j] = matrix_in[i][j]
                elif j == np.size(matrix_in, 1):
                    matrix_out[i][j] = -matrix_in[i][j-1]
                else:
                    matrix_out[i][j] = matrix_in[i][j] - matrix_in[i][j-1]  # Asignación de valor a matrix_out
            except Exception as e:
                print(i, j, e)
                exit(12)
    return matrix_out


def matrix_file_reader(filename):
    """
    Lee un archivo y lo forma un numpy.ndarray con sus valores.
    :param filename: Nombre del archivo a leer. Este sera leido usando como ubicacion base la ubicacion del archivo que
    llame a esta funcion.
    :return: numpy.ndarray si el archivo era valido. None si no.
    """
    matrix = None
    matrix_values_list = []     # Lista que almacena los valores hasta que se conoce el tamaño de la matriz de entrada.
    matrix_values_list_alt = []
    columns = 0
    rows = 0

    if os.path.isfile(filename):
        with open(filename, 'r', newline='\n') as file:
            for line in file:
                rows = rows + 1                             # Cuenta las filas
                line_array = line.split()                   # Forma una lista de variables en la fila.
                matrix_values_list = matrix_values_list + line_array
                if columns == 0:
                    columns = len(line_array)               # Reconoce las columnas. Si alguna fila tiene mas valores,
                    # estos no se tomaran en cuenta.
        for i, value in enumerate(matrix_values_list):
            matrix_values_list_alt[i] = int(value)
        matrix = np.asarray(matrix_values_list_alt)             # Forma un ndarray en base a la lista.
        matrix = np.reshape(matrix, (rows, columns))        # Cambia la forma del ndarray en base a rows y columns.
    else:
        print("Archivo no soportado.")
    return matrix


def main():
    filename = "input.txt"
    foo = matrix_file_reader(filename)
    print("Entrada:\n", foo, "\n")
    if foo is not None:
        print("\n", alt_matrix_generator(foo))


if __name__ == '__main__':
    main()
