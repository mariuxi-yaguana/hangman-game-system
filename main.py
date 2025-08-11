import random

palabras = ["ecuador", "sistema", "ingenieria", "ahorcado", "logica"]
palabra = random.choice(palabras)
letras_adivinadas = []
intentos = 6

print("🎮 Bienvenido al Hangman Game System 🎮")
print("Adivina la palabra letra por letra.")

def mostrar_tablero():
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    print(tablero.strip())

while intentos > 0:
    mostrar_tablero()
    letra = input("Ingresa una letra: ").lower()

    if letra in palabra and letra not in letras_adivinadas:
        letras_adivinadas.append(letra)
        print("✅ ¡Bien hecho!")
    elif letra in letras_adivinadas:
        print("⚠ Ya ingresaste esa letra.")
    else:
        intentos -= 1
        print(f"❌ Incorrecto. Te quedan {intentos} intentos.")

    if all(letra in letras_adivinadas for letra in palabra):
        print(f"🎉 ¡Ganaste! La palabra era '{palabra}'.")
        break
else:
    print (f"💀 Perdiste. La palabra era '{palabra}'.")
print(" ".join(tablero))
