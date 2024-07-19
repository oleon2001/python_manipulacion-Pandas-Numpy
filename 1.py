# Generador automático de frases
import random
import time
personas=['Juan','maria','sofia','Kevin','Oswaldo']
verbos=['ama','odia','no entiende','insulta','sonrie','escucha']
def escogePalabra(palabraLista):
   índice=random.randint(0,len(palabraLista)-1)
   return palabraLista[índice]

otrojuego='sí'
    
while otrojuego=='sí' or otrojuego=='Si' or otrojuego=='Sí' or otrojuego=='si':    
    persona=escogePalabra(personas)
    persona2=escogePalabra(personas)
    verbo=escogePalabra(verbos)
    print('Voy a decirte algo de '+persona)
    time.sleep(1)
    print()
    print(persona+ ' '+verbo+ ' a ', end='')
    time.sleep(2)
    print(persona2)
    time.sleep(2)
    print()
    print('¿Quieres que te diga otra cosa? (Escribe sí o no)')
    otrojuego=input()
print('¡Hasta luego!')   