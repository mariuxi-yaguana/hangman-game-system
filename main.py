import random

# Función principal del juego
def jugar():
    palabra_secreta = random.choice(["ecuador", "sistema", "ingenieria", "ahorcado", "logica"])
    letras_adivinadas = []
    intentos = 6
    palabra_adivinada = False

    print("🎮 Bienvenido al Hangman Game System 🎮")
    print("Adivina la palabra letra por letra.")
    print(f"🔎 Tienes {intentos} intentos. ¡Buena suerte!\n")

    while not palabra_adivinada and intentos > 0:
        try:
            letra = input("🔤 Ingresa una letra: ").lower()
            if not letra.isalpha() or len(letra) != 1:
                raise ValueError("⚠ Debes ingresar una sola letra válida.")
        except ValueError as ve:
            print("❌ Error:", ve)
            continue

        # Verificar si la letra ya fue ingresada
        if letra in letras_adivinadas:
            print("⚠ Ya ingresaste esa letra. Intenta otra.")
            continue

        letras_adivinadas.append(letra)

        # Mostrar el estado actual de la palabra
        palabra_mostrada = ""
        for letra_actual in palabra_secreta:
            if letra_actual in letras_adivinadas:
                palabra_mostrada += letra_actual + " "
            else:
                palabra_mostrada += "_ "

        print("\n🔤 Palabra:", palabra_mostrada.strip())

        # Verificar si la palabra fue adivinada
        if "_" not in palabra_mostrada:
            palabra_adivinada = True
            print("🎉 ¡Felicidades! Adivinaste la palabra.")
        elif letra not in palabra_secreta:
            intentos -= 1
            print(f"❌ La letra no está en la palabra. Te quedan {intentos} intentos.")

    if not palabra_adivinada:
        print(f"💀 Se acabaron los intentos. La palabra era: {palabra_secreta}")

# Ejecutar el juego
jugar()