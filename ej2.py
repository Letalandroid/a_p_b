import math

# Constantes para representar las piezas en Tic-Tac-Toe
X = 1
O = -1
VACIO = 0

# Evaluación de estado (simplificado)
def evaluacion_estado(tablero):
    for fila in tablero:
        if fila.count(X) == 3:
            return 10
        elif fila.count(O) == 3:
            return -10
    for col in range(3):
        if [tablero[i][col] for i in range(3)].count(X) == 3:
            return 10
        elif [tablero[i][col] for i in range(3)].count(O) == 3:
            return -10
    if [tablero[i][i] for i in range(3)].count(X) == 3 or [tablero[i][2 - i] for i in range(3)].count(X) == 3:
        return 10
    if [tablero[i][i] for i in range(3)].count(O) == 3 or [tablero[i][2 - i] for i in range(3)].count(O) == 3:
        return -10
    return 0

# Generación de movimientos (hijos)
def generar_hijos(tablero, jugador):
    hijos = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == VACIO:
                nuevo_tablero = [fila[:] for fila in tablero]  # Copiar el tablero
                nuevo_tablero[i][j] = jugador
                hijos.append(nuevo_tablero)
    return hijos

# Función Alfa-Beta
def alfa_beta(tablero, profundidad, alfa, beta, maximizando):
    score = evaluacion_estado(tablero)
    if score != 0 or profundidad == 0:
        return score

    if maximizando:
        max_eval = -math.inf
        for hijo in generar_hijos(tablero, X):  # Jugador MAX (X)
            eval = alfa_beta(hijo, profundidad - 1, alfa, beta, False)
            max_eval = max(max_eval, eval)
            alfa = max(alfa, eval)
            if beta <= alfa:
                break  # Poda
        return max_eval
    else:
        min_eval = math.inf
        for hijo in generar_hijos(tablero, O):  # Jugador MIN (O)
            eval = alfa_beta(hijo, profundidad - 1, alfa, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alfa:
                break  # Poda
        return min_eval

# Ejemplo de uso
tablero_inicial = [
    [VACIO, VACIO, VACIO],
    [VACIO, VACIO, VACIO],
    [VACIO, VACIO, VACIO]
]
mejor_jugada = alfa_beta(tablero_inicial, 9, -math.inf, math.inf, True)
print("La mejor jugada tiene una evaluación de:", mejor_jugada)
