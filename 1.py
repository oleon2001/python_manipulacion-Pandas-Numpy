"""
Generador automático de frases

Este programa genera frases aleatorias que relacionan a dos personas y un verbo.
Por ejemplo, "Juan ama a Maria" o "Sofia insulta a Kevin".

Uso:
    Ejecute el programa y responderá con una frase aleatoria.
    Luego, se preguntará si desea generar otra frase.
    Responda con "sí" o "no" para continuar o salir del programa.

Example:
    $ python frase_generator.py
    Voy a decirte algo de Juan
    Juan odia a Sofia
    ¿Quieres que te diga otra cosa? (Escribe sí o no)
    sí
    Voy a decirte algo de Maria
    Maria sonrie a Oswaldo
    ¿Quieres que te diga otra cosa? (Escribe sí o no)
    no
    ¡Hasta luego!
"""

import random
import time

personas = ['Juan', 'Maria', 'Sofia', 'Kevin', 'Oswaldo']
verbos = ['ama', 'odia', 'no entiende', 'insulta', 'sonrie', 'escucha']

def escogePalabra(palabraLista):
    """
    Escoge una palabra aleatoria de una lista.

    Args:
        palabraLista (list): Lista de palabras.

    Returns:
        str: Palabra aleatoria escogida.
    """
    indice = random.randint(0, len(palabraLista)-1)
    return palabraLista[indice]

otrojuego = 'sí'

while otrojuego == 'sí' or otrojuego == 'Si' or otrojuego == 'Sí' or otrojuego == 'si':
    persona = escogePalabra(personas)
    persona2 = escogePalabra(personas)
    verbo = escogePalabra(verbos)
    print('Voy a decirte algo de ' + persona)
    time.sleep(1)
    print()
    print(persona + ' ' + verbo + ' a ', end='')
    time.sleep(2)
    print(persona2)
    time.sleep(2)
    print()
    print('¿Quieres que te diga otra cosa? (Escribe sí o no)')
    otrojuego = input()

print('¡Hasta luego!')