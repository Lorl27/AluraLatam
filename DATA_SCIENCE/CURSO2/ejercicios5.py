# Vamos practicar lo que hemos aprendido hasta ahora resolviendo los problemas propuestos en código.

#!SECTION ERRORES: SyntaxError NameError IndexError TypeError KeyError 

# Calentamiento

# 1 - Haz un programa que solicite a la persona usuaria ingresar dos números decimales y calcular la división entre estos números. El código debe incluir un manejo de error, indicando el tipo de error que se generó si la división no es posible.

# Prueba el programa con el segundo valor numérico de la entrada igual a 0. También prueba usando caracteres textuales en la entrada para verificar los tipos de errores que ocurren.

try:
    a=float(input("nro1: \t"))
    b=float(input("nro2: \t"))

    r=a/b
except Exception as e:
    print(f"ERROR:{e}...")
else:
    print(f"la division es: {a/b}")


# 2 - Haz un programa que solicite a la persona usuaria ingresar un texto que será una clave a buscar en el siguiente diccionario: edades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, almacenando el resultado del valor en una variable. El código debe incluir un manejo de error KeyError, imprimiendo la información 'Nombre no encontrado' en caso de error, e imprimir el valor si no ocurre ninguno.

# Prueba el programa con un nombre presente en una de las claves del diccionario y con uno que no esté en el diccionario para verificar el mensaje de error.
edades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}
try:
    a=input("key: \t")

except KeyError as e:
    print(f"ERROR:{e}... Pone una key que sí este...")
else:
    print(f"El valor es: {edades[a]}")

# 3 - Crea una función que reciba una lista como parámetro y convierta todos los valores de la lista a flotantes. La función debe incluir un manejo de error indicando el tipo de error generado y devolver la lista si no ha ocurrido ningún error. Por último, debe tener la cláusula finally para imprimir el texto: 'Fin de la ejecución de la función'.

def lis(lista):
    try:
        for x in lista:
            float(x)

    except Exception as e:
        print(f"ERROR:{e}...")
    else:
        print(f"La lista es: {lista}")
    finally:
        print('Fin de la ejecución de la función')

# 4 - Crea una función que reciba dos listas como parámetros y agrupe los elementos uno a uno de las listas, formando una lista de tuplas de 3 elementos. El primer y segundo elemento de la tupla son los valores en la posición i de las listas y el tercer elemento es la suma de los valores en la posición i de las listas.

# La función debe incluir un manejo de error indicando el tipo de error generado y devolver como resultado la lista de tuplas. Si las listas enviadas como parámetro tienen tamaños diferentes, la función debe devolver un IndexError con la frase: 'La cantidad de elementos en cada lista es diferente.'.

# Datos para probar la función:

# Valores sin error:

# lista1 = [4, 6, 7, 9, 10]
# lista2 = [-4, 6, 8, 7, 9]
# Copia el código
# Listas con tamaños diferentes:

# lista1 = [4, 6, 7, 9, 10, 4]
# lista2 = [-4, 6, 8, 7, 9]
# Copia el código
# Listas con valores incoherentes:

# lista1 = [4, 6, 7, 9, 'A']
# lista2 = [-4, 'E', 8, 7, 9]

def lis2(lista,lista2):
    try:
        if(len(lista)!=len(lista2)):
            raise IndexError("LISTAS CON DIFERENTES TAMAÑOS")
        
        for x,y in zip(lista,lista2):
            t=tuple(x,y,x+y)

    except Exception as e:
        print(f"ERROR:{e}...")
    else:
        print(f"La tupla es: {t}")
    finally:
        print('Fin de la ejecución de la función')


# Aplicando a proyectos

# 5 - Como desafío, se te ha asignado la tarea de desarrollar un código que contabiliza las puntuaciones de estudiantes de una institución educativa de acuerdo con sus respuestas en una prueba. Este código debe ser probado para un ejemplo de 3 estudiantes con una lista de listas en la que cada lista tiene las respuestas de 5 preguntas objetivas de cada estudiante. Cada pregunta vale un punto y las alternativas posibles son A, B, C o D.

# Si alguna alternativa en una de las pruebas no está entre las alternativas posibles, debes lanzar un ValueError con el mensaje "La alternativa [alternativa] no es una opción de alternativa válida". El cálculo de las 3 notas solo se realizará mediante las entradas con las alternativas A, B, C o D en todas las pruebas. Si no se lanza la excepción, se mostrará una lista con las notas en cada prueba.

# Datos para la prueba del código:

# Respuestas de la prueba:

# respuestas = ['D', 'A', 'B', 'C', 'A']
# Copia el código
# A continuación, hay 2 listas de listas que puedes usar como prueba:

# Notas sin excepción:

# tests_sin_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
# Copia el código
# Notas con excepción:

# tests_con_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

respuesta = ['D', 'A', 'B', 'C', 'A']

def corrector(tests: list):
  puntuaciones = [] 
  try:
    for test in tests:
      nota = 0 
      for i in range(len(test)):
        if test[i] not in ['A', 'B', 'C', 'D']:
          raise ValueError(f'La alternativa {test[i]} no es una opción de alternativa válida')
        elif test[i] == respuesta[i]: 
          nota += 1
      puntuaciones.append(nota) 
  except Exception as e:
    print(e)
  else:
    return puntuaciones 

# 6 - Estás trabajando con procesamiento de lenguaje natural (NLP) y, en esta ocasión, tu líder te pidió que crees un fragmento de código que reciba una lista con las palabras separadas de una frase generada por ChatGPT.

# Necesitas crear una función que evalúe cada palabra de este texto y verifique si el tratamiento para quitar los símbolos de puntuación (',', '.', '!' y '?') se realizó. De lo contrario, se lanzará una excepción del tipo ValueError señalando el primer caso en que se detectó el uso de una puntuación a través de la frase "El texto presenta puntuaciones en la palabra "[palabra]"". Esta solicitud se centra en el análisis del patrón de frases generadas por la inteligencia artificial.

# Datos para probar el código:

# Lista tratada:

# lista_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso', 'versátil',
#                   'y', 'fácil', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos', 'desde',
#                   'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial']
# Copia el código
# Lista no tratada:

# lista_no_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso,', 'versátil',
#                   'y', 'fácil,', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos,', 'desde',
#                   'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial!']

def evaluar_puntuacion(lista_palabras):
    try:
        for palabra in lista_palabras:
            if any(puntuacion in palabra for puntuacion in [',', '.', '!', '?']):
                raise ValueError(f"El texto presenta puntuaciones en la palabra '{palabra}'.")
    except ValueError as e:
        print(f"Error: {e}")
        
        
        
#"""7"""
# Creando la función que recibe las dos listas y la operación a realizar
def divide_columnas(lista_1: list, lista_2: list) -> list:
  # try-except que verifica si es posible calcular la división y lanza una excepción si las listas tienen tamaños diferentes
  # o si hay alguna división por cero en uno de los cálculos entre los números de las listas
  try:
    if len(lista_1) != len(lista_2):  # Verificando si las listas tienen el mismo tamaño, si no, lanza una excepción
      raise ValueError("Las listas deben tener el mismo tamaño")

    # La función zip empareja los elementos de las listas y se genera una lista mediante la división entre las parejas
    resultado = [round(a / b, 2) for a, b in zip(lista_1, lista_2)]
  except ValueError as e:
    print(e)
  except ZeroDivisionError as e:
    print(f"{e}: La 2ª lista no puede tener un valor igual a 0")
  else:
    return resultado