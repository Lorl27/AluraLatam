# Vamos practicar el uso de estructuras de repetición como el "while" y el "for" a partir de algunas actividades. Ahora que estamos avanzando en el contenido, podemos hacer los desafíos más interesantes. ¡Para ello, trabajaremos en proyectos de código!

# Comencemos resolviendo algunos problemas para calentar y prepararnos para los proyectos.

# Entrenando la programación

# 1 - Escribe un programa que solicite dos números enteros e imprima todos los números enteros entre ellos.
a=int(input("1"))
b=int(input("2"))
contador=a
while(contador<b):
    contador=+1
    print(contador)

# 2 - Escribe un programa para calcular cuántos días tomará que la colonia de una bacteria A supere o iguale a la colonia de una bacteria B, basado en tasas de crecimiento del 3% y 1.5%, respectivamente. Supón que la colonia A comienza con 4 elementos y B con 10.
colA=4
colB=10
cont=0
while(colA<colB):
    colA*=0.3
    colB*=0.15
    cont=+1

print(cont)

# 3 - Para procesar una cantidad de 15 datos de evaluaciones de usuarios de un servicio de la empresa, necesitamos verificar si las calificaciones son válidas. Por lo tanto, escribe un programa que recibirá calificaciones del 0 al 5 y verificará si son valores válidos. Si se ingresa una calificación superior a 5 o inferior a 0, se repetirá hasta que el usuario ingrese un valor válido.

calificacion=int(input("c"))
while(calificacion<0 or calificacion>5):
    calificacion=int(input("c"))

# 4 - Desarrolla un programa que lea un conjunto indefinido de temperaturas en grados Celsius y calcule su promedio. La lectura debe detenerse al ingresar el valor -273°C.
suma=0
cant=0
temp=int(input("se termina en -273"))
while(temp!=-273):
    suma+=temp
    cant+=1
    temp=int(input("se termina en -273"))

print(f"promedio: {suma/cant}")

# 5 - Escribe un programa que calcule el factorial de un número entero proporcionado por el usuario. Recuerda que el factorial de un número entero es el producto de ese número por todos sus antecesores hasta llegar al número 1. Por ejemplo, el factorial de 5 es 5 x 4 x 3 x 2 x 1 = 120.

num = int(input('Ingresa un número entero: '))

factorial = 1

i = num
while i > 0:
    factorial *= i
    i -= 1

# Imprime el cálculo del factorial
print(f'El factorial de {num} es {factorial}')

# Momento de los proyectos

# 6 - Escribe un programa que genere la tabla de multiplicar de un número entero del 1 al 10, según la elección del usuario. Como ejemplo, para el número 2, la tabla de multiplicar debe mostrarse en el siguiente formato:

# Tabla de multiplicar del 2:
# 2 x 1 = 2
# 2 x 2 = 4
# [...]
# 2 x 10 = 20

n=int(input("mult"))

for x in range(1,10+1):
    print(n*x)

# 7 - Los números primos tienen diversas aplicaciones en Ciencia de Datos, como en criptografía y seguridad. Un número primo es aquel que es divisible solo por sí mismo y por 1. Por lo tanto, crea un programa que solicite un número entero y determine si es un número primo o no.

# Recopilamos el número
num = int(input('Ingresa un número entero: '))

# Los números enteros iguales o menores que 1 no se consideran primos
if num > 1:
    for i in range(2, num):
        # Verificamos todos los residuos de la división entre todos los números menores que num
        # Si algún residuo es 0, significa que es divisible por otro número además de sí mismo y 1
        if (num % i) == 0:
            print(f'{num} no es un número primo')
            break
    else:
        print(f'{num} es un número primo')
else:
    print(f'{num} no es un número primo')

# 8 - Vamos a comprender la distribución de edades de los pensionistas de una empresa de seguros. Escribe un programa que lea las edades de una cantidad no informada de clientes y muestre la distribución en los intervalos [0-25], [26-50], [51-75] y [76-100]. La entrada de datos se detendrá al ingresar un número negativo.

n=int(input("mult"))
rango_0_25=0
rango_26_50=0
rango_51_75=0
rango_76_100=0
while(n>=0):
    if n in range(0,25+1):
        rango_0_25+=1
    if n in range(26,51):
        rango_26_50=+1
    if n in range(51,75+1):
        rango_51_75+=1
    if n in range(76,100+1):
        rango_76_100_100+=1
        
    n=int(input("mult"))
    
print(f"RANGOS: [0-25]:{rango_0_25} -- [26-50]:{rango_26_50} -- [51-75]:{rango_51_75} -- [76-100]:{rango_76_100}")

# 9 - En una elección para la gerencia de una empresa con 20 empleados, hay cuatro candidatos. Escribe un programa que calcule al ganador de la elección. La votación se realizó de la siguiente manera:

# Cada empleado votó por uno de los cuatro candidatos (representados por los números 1, 2, 3 y 4).

# También se contaron los votos nulos (representados por el número 5) y los votos en blanco (representados por el número 6).

# Al final de la votación, el programa debe mostrar el número total de votos para cada candidato, los votos nulos y los votos en blanco. Además, debe calcular y mostrar el porcentaje de votos nulos con respecto al total de votos y el porcentaje de votos en blanco con respecto al total de votos.

votos_nulos=0
votos_blancos=0
votos_total=0
voto1=0
voto2=0
voto3=0
voto4=0

voto=int(input("1 al 6"))
while(contador!=20):
    if(voto==5):
        votos_nulos+=1
    if(voto==6):
        votos_blancos+=1
    if(voto==1):
        voto1+=1    
    if(voto==2):
        voto2+=1  
    if(voto==3):
        voto3+=1
    if(voto==4):
        voto4+=1
    contador+=1
    voto=int(input("1 al 6"))

def win(a,b,c,d):
    if(a>b and a>c and a>d):
        return a
    if(a<b and b>c and b>d):
        return b
    if(c>b and a<c and c>d):
        return c
    else:
        return d
print(f"VOTOS TOTALES:{contador} -- GANADOR: {win(voto1,voto2,voto3,voto4)} -- NULOS: {votos_nulos/contador}-- BLANCOS: {votos_blancos/contador}")