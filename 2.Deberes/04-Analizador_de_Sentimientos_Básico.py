# Mejora el analizador de sentimientos para manejar oraciones con múltiples emociones, 
# asignando diferentes ponderaciones a las palabras según su intensidad 
# (por ejemplo, "genial" podría tener más peso que "bien").

ponderaciones_positivas = {
    "bien": 1,
    "genial": 2,
    "fantástico": 3,
    "excelente": 3,
    "feliz": 2
}

ponderaciones_negativas = {
    "mal": 1,
    "terrible": 2,
    "horrible": 3,
    "malo": 2,
    "triste": 1
}

def analizar_sentimiento(texto):
    texto = texto.lower()

    # Calcular puntaje total positivo y negativo
    puntaje_positivo = sum(ponderaciones_positivas.get(palabra, 0) for palabra in texto.split() if palabra in ponderaciones_positivas)
    puntaje_negativo = sum(ponderaciones_negativas.get(palabra, 0) for palabra in texto.split() if palabra in ponderaciones_negativas)

    # Determinar el sentimiento basado en los puntajes
    if puntaje_positivo > puntaje_negativo:
        return "Sentimiento positivo"
    elif puntaje_negativo > puntaje_positivo:
        return "Sentimiento negativo"
    else:
        return "Sentimiento neutral"

# Ejemplo de uso
texto = input("Escribe una oración para analizar: ")
resultado = analizar_sentimiento(texto)
print(f"El resultado del análisis es: {resultado}")