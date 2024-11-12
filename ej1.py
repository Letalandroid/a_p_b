import math
import random

# Función de evaluación de un estado del tablero (simplificado)
def evaluacion_estado(tablero):
    return random.randint(-10, 10)  # Devuelve un valor aleatorio (para ilustrar)

# Generar estados hijos (simulación)
def generar_hijos(tablero, jugador):
    # Simulamos la generación de movimientos, simplemente con +1 o -1 al valor del tablero
    return [tablero + 1, tablero - 1]  # Cada jugador tiene dos opciones de movimiento

# Algoritmo Alfa-Beta recursivo
def alfa_beta(tablero, profundidad, alfa, beta, maximizando):
    if profundidad == 0:  # Si llegamos a la profundidad máxima o fin del juego
        return evaluacion_estado(tablero)

    if maximizando:
        max_eval = -math.inf
        for hijo in generar_hijos(tablero, 1):  # Jugador 1 (MAX)
            eval = alfa_beta(hijo, profundidad - 1, alfa, beta, False)
            max_eval = max(max_eval, eval)
            alfa = max(alfa, eval)
            if beta <= alfa:
                break  # Poda
        return max_eval
    else:
        min_eval = math.inf
        for hijo in generar_hijos(tablero, -1):  # Jugador 2 (MIN)
            eval = alfa_beta(hijo, profundidad - 1, alfa, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alfa:
                break  # Poda
        return min_eval

# Ejemplo de uso
tablero_inicial = 0  # Representación simple del tablero
profundidad_maxima = 3  # Limitar la búsqueda a 3 niveles de profundidad
mejor_jugada = alfa_beta(tablero_inicial, profundidad_maxima, -math.inf, math.inf, True)
print("La mejor jugada tiene una evaluación de:", mejor_jugada)
