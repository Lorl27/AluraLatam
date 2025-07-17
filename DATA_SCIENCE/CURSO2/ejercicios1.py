# Vamos a practicar lo que hemos aprendido hasta ahora resolviendo los problemas propuestos en código.

# Calentamiento

# 1 - Escribe un código para instalar la versión 3.7.1 de la biblioteca matplotlib.

#pip install matplotlib
import matplotlib as mpl


# 2 - Escribe un código para importar la biblioteca numpy con el alias np.
# pip install numpy
import numpy as np

# 3 - Crea un programa que lea la siguiente lista de números y elija uno al azar.

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

import random
print(random.choice(lista))

# 4 - Crea un programa que genere aleatoriamente un número entero menor que 100.

print(random.randrange(0,100))

# 5 - Crea un programa que solicite a la persona usuaria ingresar dos números enteros y calcule la potencia del primer número elevado al segundo.

import math
a = int(input("Primer numero: \n"))
b = int(input("Segundo numero: \n"))

print(math.pow(a,b))

# Aplicando a proyectos

# 6 - Se debe escribir un programa para sortear a un seguidor de una red social para ganar un premio. La lista de participantes está numerada y debemos elegir aleatoriamente un número según la cantidad de participantes. Pide a la persona usuaria que proporcione el número de participantes del sorteo y devuelve el número sorteado.

n = int(input("Nro participantes:... \n"))
print(random.randrange(0,n+1))

# 7 - Has recibido una solicitud para generar números de token para acceder a la aplicación de una empresa. El token debe ser par y variar de 1000 a 9998. Escribe un código que solicite el nombre de la persona usuaria y muestre un mensaje junto a este token generado aleatoriamente.

nombre_usuario=input("Ingresa tu nombre de usuario: \n")
token_generado=random.randrange(1000,9998+1,2)

print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")


# 8 - Para diversificar y atraer nuevos clientes, una lanchonete creó un ítem misterioso en su menú llamado "ensalada de frutas sorpresa". En este ítem, se eligen aleatoriamente 3 frutas de una lista de 12 para componer la ensalada de frutas del cliente. Crea el código que realice esta selección aleatoria según la lista dada.

frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

item=random.sample(frutas,3)
print(item)


# 9 - Has recibido un desafío para calcular la raíz cuadrada de una lista de números, identificando cuáles resultan en un número entero. La lista es la siguiente:

numeros = [2, 8, 15, 23, 91, 112, 256]

for x in numeros:
    if (math.sqrt(x)%1==0):
        print(f"el cuadrado de {x} es entero => {math.sqrt(x)}")

raices_enteras = [num for num in numeros if math.sqrt(num) % 1 == 0]
print("Números con raíces enteras:", raices_enteras)

# 10 - Haz un programa para una tienda que vende césped para jardines. Esta tienda trabaja con jardines circulares y el precio del metro cuadrado de césped es de R$ 25,00. Pide a la persona usuaria el radio del área circular y devuelve el valor en reales de cuánto tendrá que pagar.

circ_p=25.00
n=float(input("Ingresa el radio del area circular: \n"))

print(f"El area es: {math.round((math.pow(n,2)*math.pi)*circ_p,2)}")