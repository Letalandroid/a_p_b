import math

# Evaluación de una mano (simplificada)
def evaluacion_estado(mano):
    valores = [carta[0] for carta in mano]
    if valores.count('A') == 3:
        return 100  # Mano ganadora
    return sum([1 for carta in valores if carta == 'A'])  # Contar ases

# Generar manos sucesoras
def generar_hijos(mano):
    cartas_posibles = ['A', 'K', 'Q', 'J', '10']
    hijos = []
    for carta in cartas_posibles:
        hijos.append(mano + [carta])
    return hijos

# Alfa-Beta para el póker
def alfa_beta(mano, profundidad, alfa, beta, maximizando):
    score = evaluacion_estado(mano)
    if profundidad == 0:
        return score

    if maximizando:
        max_eval = -math.inf
        for hijo in generar_hijos(mano):
            eval = alfa_beta(hijo, profundidad - 1, alfa, beta, False)
            max_eval = max(max_eval, eval)
            alfa = max(alfa, eval)
            if beta <= alfa:
                break  # Poda
        return max_eval
    else:
        min_eval = math.inf
        for hijo in generar_hijos(mano):
            eval = alfa_beta(hijo, profundidad - 1, alfa, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alfa:
                break  # Poda
        return min_eval

# Ejemplo de uso
mano_inicial = ['A', 'K']
mejor_jugada = alfa_beta(mano_inicial, 3, -math.inf, math.inf, True)
print("La mejor jugada tiene una evaluación de:", mejor_jugada)
