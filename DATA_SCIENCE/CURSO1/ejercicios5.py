# Vamos practicar el uso de estructuras de datos, como listas y diccionarios, a través de algunas actividades. Ahora que estamos avanzando en el contenido, podemos hacer los desafíos más interesantes. ¡Para ello, trabajaremos con proyectos de código!

# Primero, resolveremos algunos problemas para calentar y prepararnos para los proyectos.

# Entrenando la programación

# 1 - Crea un programa que tenga la siguiente lista con los gastos de una empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Con estos valores, crea un programa que calcule el promedio de gastos. Sugerencia: usa las funciones integradas sum() y len().

lista= [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

print(f"promedio: {sum(lista)/len(lista)}")

# 2 - Con los mismos datos de la pregunta anterior, determina cuántas compras se realizaron por encima de 3000 reales y calcula el porcentaje con respecto al total de compras.
contador=0
for x in lista:
    if x>3000:
        contador+=1
print(f"Se realizaron {contador} compras >3000 , es decir un {contador/len(lista)}")

# 3 - Crea un código que recoja en una lista 5 números enteros aleatorios e imprima la lista. Ejemplo: [1, 4, 7, 2, 4].

lista=[]
for x in range(0,5):
    lista.append(int(input(f"ingrese elemento {x}")))
print(lista)

# 4 - Recoge nuevamente 5 números enteros e imprime la lista en orden inverso al enviado.

lista=[]
for x in range(0,5):
    lista[x]=input(f"ingrese elemento {x}")
print(lista[::-1])

# 5 - Crea un programa que, al ingresar un número cualquiera, genere una lista que contenga todos los números primos entre 1 y el número ingresado.

# Recopilamos el número
numero = int(input('Ingresa un número entero: '))
# Lista para almacenar los números primos
lista_primos = []
# Bucle que recorre todos los números por debajo del número ingresado
for num in range(2, numero):
  # Primo es una bandera que nos permite saber si el valor analizado es primo o no.
  primo = True
  # Probamos si todos los números por debajo del especificado en el primer bucle pueden dar una división exacta.
  for prueba_divisibles in range(2, num):
    if num % prueba_divisibles == 0:
      # Si es divisible por algún número, entendemos que el número no es primo y terminamos el bucle interno con break.
      primo = False
      break
  # La condición se convierte en el resultado booleano de primo: False. Ignoramos la condición True y ejecutamos el bloque del if.
  if primo:
    lista_primos.append(num)
# Resultado
print(f'Lista de números primos: {lista_primos}')

# 6 - Escribe un programa que pida una fecha, especificando el día, mes y año, y determine si es válida para su análisis.

fecha = input("Ingrese la fecha (dd-mm-aaaa): ")
try:
    dia, mes, anio = map(int, fecha.split("-"))
    if not (1 <= dia <= 31):
        print("DÍA INVÁLIDO")
    else:
        print("DÍA VÁLIDO")

    if not (1 <= mes <= 12):
        print("MES INVÁLIDO")
    else:
        print("MES VÁLIDO")

    if not (2000 <= anio <= 9999):
        print("AÑO INVÁLIDO")
    else:
        print("AÑO VÁLIDO")
except:
    print("Formato de fecha incorrecto.")


# Momento para los proyectos

# 7 - Para un estudio sobre la multiplicación de bacterias en una colonia, se recopiló el número de bacterias multiplicadas por día y se puede observar a continuación: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Con estos valores, crea un código que genere una lista que contenga el porcentaje de crecimiento de bacterias por día, comparando el número de bacterias en cada día con el número de bacterias del día anterior. Sugerencia: para calcular el porcentaje de crecimiento, utiliza la siguiente ecuación: 100 * (muestra_actual - muestra_anterior) / muestra_anterior.

bac_dia=[1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

def porc_crec(muestra_actual,muestra_anterior):
    return (100 * (muestra_actual - muestra_anterior) / muestra_anterior)

bac_por=[]
for x in range(1,len(bac_dia)):
    bac_por.append(porc_crec(bac_dia[x],bac_dia[x-1]))

print(bac_por)

# 8 - Para una selección de productos alimenticios, debemos separar el conjunto de IDs proporcionados por números enteros, sabiendo que los productos con ID par son dulces y los que tienen ID impar son amargos. Crea un código que recoja 10 IDs. Luego, calcula y muestra la cantidad de productos dulces y amargos.

def par(x):
    if x%2==0:
        return True
    return False

x=0
lista=[]
while(x<10):
    lista.append(int(input("nro:")))
    x+=1

dulces=0
amargos=0
for x in lista:
    if par(x):
        dulces+=1
    else:
        amargos+=1

print(f"La cantidad de dulces es: {dulces} y la de amargos es: {amargos}")

# 9 - Desarrolla un programa que informe la puntuación de un estudiante de acuerdo con sus respuestas. Debe pedir la respuesta del estudiante para cada pregunta y verificar si la respuesta coincide con el resultado. Cada pregunta vale un punto y hay opciones A, B, C o D.

# Resultado del examen:
# 01 - D
# 02 - A
# 03 - C
# 04 - B
# 05 - A
# 06 - D
# 07 - C
# 08 - C
# 09 - A
# 10 - B

punto=0
examen={1:"D",2:"A",3:"C",4:"B",5:"A",6:"D",7:"C",8:"C",9:"A",10:"B"}

for x in range(1,11):
    rta=input(f"Ingrese su respuesta para la pregunta nro {x}: ")
    if rta.upper() == examen[x]:
        punto+=1

print(f"TOTAL PUNTOS : {punto}/10")


# 10 - Un instituto de meteorología desea realizar un estudio de la temperatura media de cada mes del año. Para ello, debes crear un código que recoja y almacene esas temperaturas medias en una lista. Luego, calcula el promedio anual de las temperaturas y muestra todas las temperaturas por encima del promedio anual y en qué mes ocurrieron, mostrando los meses por su nombre (Enero, Febrero, etc.).
lista=[]

def mes_fun(nro):
    if nro==0:
        return "Enero"
    elif nro==1:
        return "Febrero"
    elif nro==2:
        return "Marzo"
    elif nro==3:
        return "Abril"
    elif nro==4:
        return "Mayo"
    elif nro==5:
        return "Junio"
    elif nro==6:
        return "Julio"
    elif nro==7:
        return "Agosto"
    elif nro==8:
        return "Septiembre"
    elif nro==9:
        return "Octubre"
    elif nro==10:
        return "Noviembre"
    elif nro==11:
        return "Diciembre"

for x in range(0,12):
    lista.append(float(input(f"temperatura nro {x+1}")))
    
promedio=sum(lista)/len(lista)
for x in lista:
    if x > promedio:
        print(f"temp:{x} ocurrida en {mes_fun(lista.index(x))}")
    
# 11 - Una empresa de comercio electrónico está interesada en analizar las ventas de sus productos. Los datos de ventas se han almacenado en un diccionario:

# {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

datos_venta={'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

contador=0
max=datos_venta["Producto A"]
for key,value in datos_venta.items():
    contador+=value
    if value > max:
        max=value

print(f"maximo: {max} - ventas totales: {contador}")

# ---
# Diccionario de ventas
datos_ventas = {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

# Inicializamos las variables
total_ventas = 0  # Sumará todas las ventas
producto_mas_vendido = ''  # Almacenará el nombre del producto más vendido
unidades_producto_mas_vendido = 0  # Almacenará la cantidad más alta de ventas

# Recorremos las claves y elementos del diccionario
for producto in datos_ventas.keys():
    # Sumamos el total de ventas
    total_ventas += datos_ventas[producto]
    # Verificamos si el valor de ventas actual (datos_ventas[producto]) es mayor que el valor almacenado en unidades_producto_mas_vendido
    # Cada vez que datos_ventas[producto] supere el valor en unidades_producto_mas_vendido,
    # la variable unidades_producto_mas_vendido será igual a datos_ventas[producto], asignando un nuevo valor
    # De manera similar, producto_mas_vendido también se actualiza con el producto actual
    if datos_ventas[producto] > unidades_producto_mas_vendido:
        unidades_producto_mas_vendido = datos_ventas[producto]
        producto_mas_vendido = producto
# Resultados
print(f'Total de ventas es {total_ventas}')
print(f'{producto_mas_vendido} es el más vendido')
# ---

# Escribe un código que calcule el total de ventas y el producto más vendido.

# 12 - Se realizó una encuesta de mercado para decidir cuál diseño de marca infantil es más atractivo para los niños. Los votos de la encuesta se pueden ver a continuación:

# Tabla de votos de la marca
# Diseño 1 - 1334 votos
# Diseño 2 - 982 votos
# Diseño 3 - 1751 votos
# Diseño 4 - 210 votos
# Diseño 5 - 1811 votos

# Adapta los datos proporcionados a una estructura de diccionario. A partir de ello, informa el diseño ganador y el porcentaje de votos recibidos.

dic = {"d1":1334, "d2":982, "d3":1751, "d4":210, "d5":1811}

total_votos = sum(dic.values())
ganador = max(dic, key=dic.get)
votos_ganador = dic[ganador]
porcentaje = 100 * votos_ganador / total_votos

print(f"El ganador es {ganador} con {votos_ganador} votos ({porcentaje:.2f}%)")



# 13 - Los empleados de un departamento de tu empresa recibirán una bonificación del 10% de su salario debido a un excelente rendimiento del equipo. El departamento de finanzas ha solicitado tu ayuda para verificar las consecuencias financieras de esta bonificación en los recursos. Se te ha enviado una lista con los salarios que recibirán la bonificación: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. La bonificación de cada empleado no puede ser inferior a 200. En el código, convierte cada uno de los salarios en claves de un diccionario y la bonificación de cada salario en el valor correspondiente. Luego, informa el gasto total en bonificaciones, cuántos empleados recibieron la bonificación mínima y cuál fue el valor más alto de la bonificación proporcionada.

# Lista de salarios
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
# Inicializamos las variables
diccionario_abonos = {}  # Diccionario de abonos
total_abono = 0  # Sumará todos los gastos en abonos
abonos_minimo = 0  # Almacenará la cantidad de abonos mínimos
mayor_abono = 0  # Almacenará el mayor valor de abono

# Recorremos toda la lista de salarios
for salario in salarios:
    # Calculamos el valor teórico del abono
    abono = salario * 0.1
    # Si el abono es inferior a 200,
    # ajustamos el valor del abono al mínimo (200)
    if abono < 200:
        abono = 200
    # Agregamos un nuevo dato en el diccionario con la clave abono
    diccionario_abonos[salario] = abono

# Recorremos todos los valores del diccionario de abonos
for abono in diccionario_abonos.values():
    # Contamos los salarios mínimos
    if abono == 200:
        abonos_minimo += 1
    # Verificamos si el abono leído es mayor que el valor almacenado en mayor_abono
    # Cada vez que el abono supere el valor de mayor_abono,
    # la variable mayor_abono será igual al abono, asignando un nuevo valor
    if abono > mayor_abono:
        mayor_abono = abono
    # Sumamos los abonos
    total_abono += abono
# Resultados
print(f'Abonos: {diccionario_abonos}')
print(f'Total de gastos en abonos: {total_abono}')
print(f'Número de empleados que recibieron el abono mínimo: {abonos_minimo}')
print(f'Mayor valor de abono: {mayor_abono}')

# 14 - Un equipo de científicos de datos está estudiando la diversidad biológica en un bosque. El equipo recopiló información sobre el número de especies de plantas y animales en cada área del bosque y almacenó estos datos en un diccionario. En él, la clave describe el área de los datos y los valores en las listas corresponden a las especies de plantas y animales en esas áreas, respectivamente.

# {'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}


# Escribe un código para calcular el promedio de especies por área e identificar el área con la mayor diversidad biológica. Sugerencia: utiliza las funciones incorporadas sum() y len().

# Especificamos los datos para un diccionario
datos = {'Área Norte': [2819, 7236],
         'Área Este': [1440, 9492],
         'Área Sur': [5969, 7496],
         'Área Oeste': [14446, 49688],
         'Área Centro': [22558, 45148]}
# Inicializamos las variables
suma_media = 0  # Sumará todos los promedios
mayor_diversidad = ''  # Almacenará el área con la mayor diversidad
mayor_suma = 0  # Almacenará la mayor suma de especies
# Recorremos las claves y elementos del diccionario
for área, especies in datos.items():
    # Sumamos el número de especies en cada área utilizando la función sum
    suma_especies = sum(especies)
    # Calculamos el promedio dividiendo la suma de las especies entre la cantidad de especies
    media = suma_especies / len(especies)
    # Imprimimos
    print(f'El {área} tiene un promedio de {media} especies')
    # Verificamos si la suma de especies es mayor que el valor almacenado de mayor_suma
    # Cada vez que suma_especies supere el valor de mayor_suma,
    # la variable mayor_suma será igual a suma_especies, asignando un nuevo valor
    # De manera similar, mayor_diversidad también se actualiza
    if suma_especies > mayor_suma:
        mayor_suma = suma_especies
        mayor_diversidad = área
    # Sumamos los promedios
    suma_media += media
# La media total será la suma_media dividida por la cantidad de áreas
media_total = suma_media / len(datos)
print(f'Media general de especies: {media_total}')
print(f'Área con la mayor diversidad biológica: {mayor_diversidad}')

# 15 - El departamento de Recursos Humanos de tu empresa te pidió ayuda para analizar las edades de los colaboradores de 4 sectores de la empresa. Para ello, te proporcionaron los siguientes datos:

# {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
#  'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
#  'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
#  'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}


# Dado que cada sector tiene 10 colaboradores, construye un código que calcule la media de edad de cada sector, la edad media general entre todos los sectores y cuántas personas están por encima de la edad media general.

# Especificamos los datos para un diccionario
datos = {'Sector A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
        'Sector B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
        'Sector C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
        'Sector D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
# Inicializamos la variable que sumará todas las edades
total_edades = 0
# Recorremos las claves y elementos del diccionario
for sector, edades in datos.items():
  # Calculamos el promedio dividiendo la suma de las edades entre la cantidad de empleados en cada sector
  media_edad = sum(edades) / len(edades)
  # Imprimimos
  print(f'El {sector} tiene un promedio de {media_edad}')
  # Sumamos los promedios
  total_edades += sum(edades)
# La media total será el total_edades dividido por la cantidad de personas totales (sectores * empleados por sector)
media_total = total_edades / (len(edades) * len(datos))
print(f'La media de edad general es {media_total}')

# Inicializamos la variable que contará a todas las personas con edades por encima de la media
arriba_media = 0
# Recorremos nuevamente las claves y elementos del diccionario
for sector, edades in datos.items():
  # Leemos los elementos (edades) dentro de cada lista de edades en el diccionario
  for edad in edades:
    # Verificamos si el valor de la edad es superior a la media total
    if edad > media_total:
      # En caso de que el valor de la edad sea superior a la media, incrementamos en uno el contador
      arriba_media += 1
# Resultado
print(f'{arriba_media} personas están por encima de la edad media general')