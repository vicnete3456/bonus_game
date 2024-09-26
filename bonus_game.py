import speech_recognition as speech_recog
from speech import speech
import random
import time

levels = {
"facil": ["agenda", "ami", "souris"],
"intermedio": ["ordinateur", "algorithme", "développeur"],
"dificil": ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"]
}

def play_game(level):
    # Seleccionar las palabras en función del nivel de dificultad
    # Si el nivel no existe, devuelve una lista vacía
    words = levels.get(level, [])
    if not words:  # Si la lista está vacía, imprime un mensaje y sale de la función
        print("Nivel de dificultad incorrecto.")
        return
    puntajes = 0
    intentos = 3
    # Bucle para cada palabra en la lista de palabras del nivel seleccionado.
    for _ in range(len(words)):
        # Selecciona una palabra al azar de la lista de palabras
        random_word = random.choice(words)
        # Imprime la palabra a pronunciar
        print(f"Por favor, pronuncie la palabra {random_word}")
        # Reconocimiento de voz por el usuario y guarda la palabra reconocida
        recog_word = speech()
        print(recog_word)  # Imprime la palabra reconocida

        if random_word == recog_word:  # Compara la palabra reconocida con la palabra seleccionada
            print("¡Así es!")  # Mensaje de acierto
            puntajes += 1  # Incrementa la puntuación
        else:  # Si no coincide la palabra
            # Mensaje de error
            print(f"Algo va mal. La palabra es: {random_word}")

        time.sleep(2)  # Pausa entre palabras para dar tiempo al usuario
    #Imprime la puntuación final del jugador
    print(f"¡Se acabó el juego! Tu puntuación es: {puntajes}/{len(words)}")
 
# Seleccione el nivel de dificultad
selected_level = input(
    "Seleccione el nivel de dificultad (facil/intermedio/dificil): ").lower()  # Pide al usuario que seleccione un nivel

play_game(selected_level)  # Inicia el juego con el nivel seleccionado