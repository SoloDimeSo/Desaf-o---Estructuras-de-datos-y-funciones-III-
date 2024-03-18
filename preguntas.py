# Definición de Funciones de la funcionalidad

def obtener_pregunta_aleatoria(diccionario_preguntas):
    """Obtiene una pregunta aleatoria del diccionario de preguntas."""
    import random
    pregunta = random.choice(list(diccionario_preguntas.keys()))
    return pregunta, diccionario_preguntas[pregunta]

def mostrar_pregunta(pregunta, alternativas):
    """Muestra la pregunta y las alternativas."""
    print(pregunta)
    for idx, (alternativa, _) in enumerate(alternativas):
        print(f"{idx+1}. {alternativa}")

if __name__ == '__main__':
    # Test entregado en cada requerimiento (dado por el Tech Lead)
    
    preguntas_basicas = {
        '¿Cuál es la capital de Francia?': [['Roma', 0], ['París', 1], ['Berlín', 0]],
        '¿Cuál es el océano más grande?': [['Océano Atlántico', 0], ['Océano Pacífico', 1], ['Océano Índico', 0]],
        '¿Cuál es el río más largo del mundo?': [['Amazonas', 1], ['Nilo', 0], ['Misisipi', 0]]
    }
    
    # Obtener y mostrar una pregunta aleatoria de preguntas básicas
    pregunta, alternativas = obtener_pregunta_aleatoria(preguntas_basicas)
    print("Pregunta aleatoria de nivel básico:")
    mostrar_pregunta(pregunta, alternativas)
