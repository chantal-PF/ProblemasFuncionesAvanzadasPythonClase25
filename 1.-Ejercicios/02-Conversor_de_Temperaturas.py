# Este ejercicio te ayudará a convertir temperaturas entre diferentes unidades: 
# Celsius, Fahrenheit y Kelvin. Es útil para entender cómo funcionan las conversiones de temperatura.

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Celsius":
        if unidad_destino == "Fahrenheit":
            return (valor * 9/5) + 32
        elif unidad_destino == "Kelvin":
            return valor + 273.15
    elif unidad_origen == "Fahrenheit":
        if unidad_destino == "Celsius":
            return (valor - 32) * 5/9
        elif unidad_destino == "Kelvin":
            return (valor - 32) * 5/9 + 273.15
    elif unidad_origen == "Kelvin":
        if unidad_destino == "Celsius":
            return valor - 273.15
        elif unidad_destino == "Fahrenheit":
            return (valor - 273.15) * 9/5 + 32

# Ejemplo de uso
valor = float(input("Ingresa el valor de la temperatura: "))
unidad_origen = input("Ingresa la unidad de origen (Celsius, Fahrenheit, Kelvin): ")
unidad_destino = input("Ingresa la unidad de destino (Celsius, Fahrenheit, Kelvin): ")

resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
print(f"{valor} {unidad_origen} son {resultado:.2f} {unidad_destino}")