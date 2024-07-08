import random

def generar_contrasena(longitud, caracteres):
  """
  Genera una contraseña aleatoria con la longitud y caracteres especificados.

  Args:
    longitud: La longitud deseada para la contraseña (int).
    caracteres: Cadenas que contienen los grupos de caracteres a incluir (str).

  Returns:
    Contraseña generada aleatoriamente (str).
  """
  contrasena = ""
  for x in range(longitud):
    contrasena += random.choice(caracteres)
  return contrasena

# Ejemplo de uso
longitud_contrasena = 12
caracteres_minusculas = "abcdefghijklmnopqrstuvwxyz"
caracteres_mayusculas = caracteres_minusculas.upper()
caracteres_numeros = "0123456789"
caracteres_simbolos = "!@#$%^&*()_-+={}[]|;:<>,.?"

contrasena_generada = generar_contrasena(longitud_contrasena,
                                       caracteres_minusculas + 
                                       caracteres_mayusculas + 
                                       caracteres_numeros + 
                                       caracteres_simbolos)

print("Tu contraseña generada es:", contrasena_generada)
