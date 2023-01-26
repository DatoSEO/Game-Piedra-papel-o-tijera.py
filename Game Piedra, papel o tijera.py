import random

# lista de opciones de juego
opciones = ['piedra', 'papel', 'tijera']

# pedir al usuario que ingrese su elección
usuario = input("Ingresa tu elección (piedra, papel o tijera): ")

# generar elección aleatoria para la computadora
computadora = random.choice(opciones)

# comparar elecciones para determinar ganador
if usuario == computadora:
    resultado = "Empate"
elif usuario == "piedra" and computadora == "tijera":
    resultado = "Gana el usuario"
elif usuario == "papel" and computadora == "piedra":
    resultado = "Gana el usuario"
elif usuario == "tijera" and computadora == "papel":
    resultado = "Gana el usuario"

else:
 resultado = "Gana la computadora"

print("Elección del usuario: " + usuario)
print("Elección de la computadora: " + computadora)
print("Resultado: " + resultado)
