# amos a practicar lo que hemos aprendido hasta ahora resolviendo los problemas propuestos en código.

# Calentamiento

# 1 - Escribe un código que lee la lista siguiente y realiza:

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
# # 1. Leer el tamaño de la lista
# # 2. Leer el valor máximo y mínimo
# # 3. Calcular la suma de los valores de la lista
# # 4. Mostrar un mensaje al final: La lista tiene `tamano` números, donde el mayor 
# # es `mayor` y el menor es `menor`. La suma de los valores es `suma`.

def max_min(lista):
    maxim=lista[0]
    minin=lista[0]
    for x in lista:
        if x>maxim:
            maxim=x
        if x<minin:
            minin=x
    return (maxim,minin)

mayor,menor=max_min(lista)
print(f"La lista ({lista}) tiene {len(lista)} números, donde el mayor es {mayor} y el menor es {menor}. La suma de los valores es {sum(lista)}.")

# 2 - Escribe una función que genere la tabla de multiplicar de un número entero del 1 al 10, según la elección del usuario. Como ejemplo, para el número 7, la tabla de multiplicar se debe mostrar en el siguiente formato:

# # Tabla del  7:
# # 7 x 0 = 0
# # 7 x 1 = 7
# # [...]
# # 7 x 10 = 70

n=int(input("Ingrese su numero: \t"))
def tabla(n):
    print(f""" TABLA DEL {n}:\n""")   
    for x in range(0,11):
        print(f""" {n} X {x} = {n*x}""")
        
tabla(n)

# 3 - Crea una función que lea la siguiente lista y devuelva una nueva lista con los múltiplos de 3:

l= [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

l2=list(filter(lambda x:x%3==0,l))  #l2=[x for x in l if x%3==0]

print(l2)

# 4 - Crea una lista de los cuadrados de los números de la siguiente lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Recuerda utilizar las funciones lambda y map() para calcular el cuadrado de cada elemento de la lista.

lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l3=list(map(lambda x:x*x,lista))

print(l3)

# Aplicando a proyectos

# 5 - Has sido contratado como científico(a) de datos de una asociación de skate. Para analizar las notas recibidas por los skaters en algunas competiciones a lo largo del año, necesitas crear un código que calcule la puntuación de los atletas. Para ello, tu código debe recibir 5 notas ingresadas por los jueces.

notas = [float(input(f"Ingrese la nota {i + 1}: ")) for i in range(5)]
notas.sort()
media = sum(notas[1:4]) / 3
print(f"Nota de la maniobra: {media:.2f}")

# 6 - Para cumplir con una demanda de una institución educativa para el análisis del rendimiento de sus estudiantes, necesitas crear una función que reciba una lista de 4 notas y devuelva:

# # mayor nota
# # menor nota
# # media
# # situación (Aprobado(a) o Reprobado(a))
# # Uso de la función
# # Mostrar: El estudiante obtuvo una media de `media`, con la mayor nota de `mayor` puntos y la menor nota de `menor` puntos y fue `situacion`.)


# def situacion(nota):
#     if nota>=6:
#         return "Aprobado/a"
#     else:
#         return "Reprobado/a"

def media(lista):
    return sum(lista)/len(lista)

def rendimiento(lista):
    prom=media(lista)
    situacion = "Aprobado" if prom >= 6 else "Reprobado"

    print(f"El estudiante obtuvo una media de {prom} con la mayor nota de {max_min(lista)[0]} puntos y la menor nota de {max_min(lista)[1]} puntos con situación: {situacion}")

rendimiento([1,4,9,10])

# 7 - Has recibido una demanda para tratar 2 listas con los nombres y apellidos de cada estudiante concatenándolos para presentar sus nombres completos en la forma Nombre Apellido. Las listas son:

nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

# # Normalizar nombres y apellidos y crear una nueva lista con los nombres completos
# # Puedes apoyarte en la función map()

def normalizar(lista_nombres,lista_apellidos):
    normal_nombre=list(map(lambda x: x.capitalize(),lista_nombres))
    normal_apellidos=list(map(lambda x: x.capitalize(),lista_apellidos))
    
    lista_completa=[]
    for x,y in zip(normal_nombre,normal_apellidos):
        lista_completa.append(x +" "+y)
    return lista_completa

#nombres_completos = list(map(lambda x, y: f"Nome completo: {x} {y}", nombres_normalizados, sobrenombres_normalizados))

print(normalizar(nombres,apellidos))

# 8 - Como científico de datos en un equipo de fútbol, necesitas implementar nuevas formas de recopilación de datos sobre el rendimiento de los jugadores y del equipo en su conjunto. Tu primera acción es crear una forma de calcular la puntuación del equipo en el campeonato nacional a partir de los datos de goles marcados y recibidos en cada juego.

# Escribe una función llamada calcula_puntos() que recibe como parámetros dos listas de números enteros, representando los goles marcados y recibidos por el equipo en cada partido del campeonato. La función debe devolver la puntuación del equipo y el rendimiento en porcentaje, teniendo en cuenta que la victoria vale 3 puntos, el empate 1 punto y la derrota 0 puntos.

# Nota: si la cantidad de goles marcados en un partido es mayor que los recibidos, el equipo ganó. En caso de ser igual, el equipo empató, y si es menor, el equipo perdió. Para calcular el rendimiento, debemos hacer la razón entre la puntuación del equipo y la puntuación máxima que podría recibir.

# Para la prueba, utiliza las siguientes listas de goles marcados y recibidos:

goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]
# # Texto probablemente mostrado:
# # La puntuación del equipo fue `puntos` y su rendimiento fue `desempeno`%"

def calcular_res(gol_m,gol_r):
    if(gol_m>gol_r):
        resultado="Ganador"
    elif(gol_m==gol_r):
        resultado="Empate"
    else:
        resultado="Perdió"
        
    return resultado

def calcula_puntos(gol_m,gol_r):
    vic=3
    emp=1
    derrot=0
    puntos=0
    for x,y in zip(gol_m,gol_r):
        r=calcular_res(x,y)
        if(r=="Ganador"):
            puntos+=vic
        elif(r=="Perdió"):
            puntos+=derrot
        else:
            puntos+=emp
            
    desempenio=(puntos/vic*len(gol_m))*100
    print(f"La puntuación del equipo fue {puntos} y su rendimiento fue {round(desempenio,2)}%")

calcula_puntos(goles_marcados,goles_recibidos)

# 9 - Te han desafiado a crear un código que calcule los gastos de un viaje a una de las cuatro ciudades desde Recife, siendo ellas: Salvador, Fortaleza, Natal y Aracaju.

# El costo diario del hotel es de 150 reales en todas ellas y el consumo de gasolina en el viaje en coche es de 14 km/l, siendo que el precio de la gasolina es de 5 reales por litro. Los gastos con paseos y alimentación a realizar en cada una de ellas por día serían [200, 400, 250, 300], respectivamente.

# Sabiendo que las distancias entre Recife y cada una de las ciudades son aproximadamente [850, 800, 300, 550] km, crea tres funciones: la primera función calcula los gastos de hotel (gasto_hotel), la segunda calcula los gastos de gasolina (gasto_gasolina) y la tercera los gastos de paseo y alimentación (gasto_paseo).

# Para probar, simula un viaje de 3 días a Salvador desde Recife. Considera el viaje de ida y vuelta en coche.

# # Texto probablemente mostrado:
# # Con base en los gastos definidos, un viaje de [dias] días a [ciudad] desde 
# # Recife costaría [gastos] reales.

km=[850, 800, 300, 550] 
p_a=[200, 400, 250, 300]

def gasto_hotel(dias):
    return 150*dias

def gasto_galosina(ciudad):
    calculo=km[ciudad]/14
    costo=calculo*5
    
    return round((costo*2),2) #ida y vuelta

def gasto_paseo(dias,ciudad):
    calculo=p_a[ciudad]*dias
    return calculo

def viaje_costo(dias,ciudad2):
    gasto=gasto_galosina(ciudad2)+gasto_hotel(dias)+gasto_paseo(dias,ciudad2)
    print(f""" Con base en los gastos definidos,
                un viaje de {dias} días a {ciudad[ciudad2]} desde 
                Recife costaría {round(gasto,2)} reales.""")

ciudad=["Salvador","EL","AN","OP"]

viaje_costo(3,ciudad.index("Salvador"))

# 10 - Has comenzado una pasantía en una empresa que trabaja con procesamiento de lenguaje natural (NLP). Tu líder te solicitó que crees un fragmento de código que reciba una frase escrita por el usuario y filtre solo las palabras con un tamaño mayor o igual a 5, mostrándolas en una lista. Esta demanda se centra en el análisis del patrón de comportamiento de las personas al escribir palabras de esta cantidad de caracteres o más.

# Consejo: utiliza las funciones lambda y filter() para filtrar estas palabras. Recordando que la función integrada filter() recibe una función (en nuestro caso, una función lambda) y filtra un iterable según la función. Para tratar la frase, utiliza replace() para cambiar ',' '.', '!' y '?' por espacio.

# Utiliza la frase="Aprender Python aquí en Alura es muy bueno" para probar el código.

frase="Aprender Python aquí en Alura es muy bueno"

def filtrar_p(palabras):
    for x in ",.!?":
        palabras=palabras.replace(x, "")
    palabras=palabras.split()
    return list(filter(lambda x: len(x)>=5,palabras))

print(filtrar_p(frase))