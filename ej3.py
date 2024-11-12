import math
import random

# Simulamos la evaluación de la serpiente
def evaluacion_estado(serpiente, comida):
    # Calculamos la longitud de la serpiente y su proximidad a la comida
    longitud = len(serpiente)
    distancia_comida = abs(serpiente[0][0] - comida[0]) + abs(serpiente[0][1] - comida[1])
    return longitud - distancia_comida  # Queremos maximizar la longitud y minimizar la distancia

# Generación de movimientos posibles (simulación de las direcciones posibles)
def generar_hijos(serpiente):
    # Simulamos 4 direcciones posibles
    return [
        [(serpiente[0][0] + 1, serpiente[0][1])] + serpiente,  # Movimiento a la derecha
        [(serpiente[0][0] - 1, serpiente[0][1])] + serpiente,  # Movimiento a la izquierda
        [(serpiente[0][0], serpiente[0][1] + 1)] + serpiente,  # Movimiento abajo
        [(serpiente[0][0], serpiente[0][1] - 1)] + serpiente   # Movimiento arriba
    ]

# Alfa-Beta para el juego de la serpiente
def alfa_beta(serpiente, comida, profundidad, alfa, beta, maximizando):
    score = evaluacion_estado(serpiente, comida)
    if profundidad == 0:  # Fin de la búsqueda
        return score

    if maximizando:
        max_eval = -math.inf
        for hijo in generar_hijos(serpiente):
            eval = alfa_beta(hijo, comida, profundidad - 1, alfa, beta, False)
            max_eval = max(max_eval, eval)
            alfa = max(alfa, eval)
            if beta <= alfa:
                break  # Poda
        return max_eval
    else:
        min_eval = math.inf
        for hijo in generar_hijos(serpiente):
            eval = alfa_beta(hijo, comida, profundidad - 1, alfa, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alfa:
                break  # Poda
        return min_eval

# Ejemplo de uso
serpiente_inicial = [(0, 0)]
comida = (5, 5)
mejor_jugada = alfa_beta(serpiente_inicial, comida, 3, -math.inf, math.inf, True)
print("La mejor jugada tiene una evaluación de:", mejor_jugada)
