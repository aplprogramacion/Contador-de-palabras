# Pedir al usuario que introduzca una frase
frase = input("En qué estás pensando? ")

# Contar el número de palabras en la frase
palabras = frase.split()
num_palabras = len(palabras)

# Imprimir el resultado
print(f"La frase '{frase}' tiene {num_palabras} palabras.")

