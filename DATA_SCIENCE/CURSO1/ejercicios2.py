# Vamos a practicar el uso de varios tipos de variables y la función input a través de algunas actividades. Resuelve los problemas propuestos en código.

# Recopilación y muestra de datos

# 1 - Crea un programa que solicite al usuario que escriba su nombre y luego imprima "Hola, [nombre]."

nombre = input("Ingresa tu nombre:")
print(f"Hola {nombre}!")

# 2 - Crea un programa que solicite al usuario que escriba su nombre y edad, y luego imprima "Hola, [nombre], tienes [edad] años."
print("Ingresa: nombre y edad")
nombre = input("Ingresa tu nombre:")
edad = input("Ingresa tu edad:")
print(f"Hola {nombre}! tenés {edad} años ;)")

# 3 - Crea un programa que solicite al usuario que escriba su nombre, edad y altura en metros, y luego imprima "Hola, [nombre], tienes [edad] años y mides [altura] metros."

print("Ingresa: nombre, edad y altura(mts)")
nombre = input("Ingresa tu nombre:")
edad = input("Ingresa tu edad:")
altura = input("Ingresa tu altura:")
print(f"Hola {nombre}! tenés {edad} años ;) y medís: {altura}")

# Calculadora con operadores

# 4 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la suma de ambos valores.
val1=input("Pon nro 1:")
val2=input("Pon nro 2:")
suma=int(val1)+int(val2)
print(f"La suma de {val1} con {val2} es: {suma}")

# 5 - Crea un programa que solicite tres valores numéricos al usuario y luego imprima la suma de los tres valores.

val1=input("Pon nro 1:")
val2=input("Pon nro 2:")
val3=input("Pon nro 3:")
suma=int(val1)+int(val2)+int(val3)
print(f"La suma de {val1} con {val2} y {val3} es: {suma}")

# 6 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la resta del primero menos el segundo valor.
val1=input("Pon nro 1:")
val2=input("Pon nro 2:")
resta=int(val1)-int(val2)
print(f"La resta de {val1} con {val2} es: {resta}")


# 7 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la multiplicación de los dos valores.

val1=input("Pon nro 1:")
val2=input("Pon nro 2:")
suma=int(val1)*int(val2)
print(f"La multiplicación de {val1} con {val2} es: {suma}")

# 8 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y realice la división entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.

val1=input("Pon nro 1:")
val2=input("Pon nro 2:")
while(val2==0):
    print("No podes divir por 0")
    val2=input("Nro 2:...")
suma=int(val1)/int(val2)
print(f"La división de {val1} con {val2} es: {suma}")

# 9 - Crea un programa que solicite dos valores numéricos, un operador y una potencia, y realice la exponenciación entre estos dos valores.
operador=input("Pon nro 1:")
potencia=input("Pon nro 2:")
suma=int(operador)**int(potencia)
print(f"La exponciación de {operador} con {potencia} es: {suma}")

# 10 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y realice la división entera entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.

numerador=input("Pon nro numerador:")
demoninador=input("Pon nro demoninador:")
while(demoninador==0):
    print("No podes divir por 0")
    demoninador=input("Nro demoninador:...")
suma=int(numerador)/int(demoninador)
print(f"La división de {numerador} con {demoninador} es: {suma}")

# 11 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y devuelva el resto de la división entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.

numerador=input("Pon nro numerador:")
demoninador=input("Pon nro demoninador:")
while(demoninador==0):
    print("No podes divir por 0")
    demoninador=input("Nro demoninador:...")
suma=int(numerador)%int(demoninador)
print(f"El resto de {numerador} con {demoninador} es: {suma}")

# 12 - Crea un código que solicite las 3 notas de un estudiante e imprima el promedio de las notas.

val1=input("Pon nro 1:")
val2=input("Pon nro 2:")
val3=input("Pon nro 3:")
suma=int(val1)+int(val2)+int(val3)
promedio=suma/3
print(f"El promedio  es: {promedio}")


# 13 - Crea un código que calcule e imprima el promedio ponderado de los números 5, 12, 20 y 15 con pesos respectivamente iguales a 1, 2, 3 y 4.

print(f"Promedio: {(5*1+12*2+20*3+15*4)/(1+2+3+4)}")


# Editando textos

# 14 - Crea una variable llamada "frase" y asígnale una cadena de texto de tu elección. Luego, imprime la frase en pantalla.

frase="Te amo"
print(frase)
# 15 - Crea un código que solicite una frase y luego imprima la frase en pantalla.
frase=input("pon tu frase:")
print(frase)

# 16 - Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en mayúsculas.
frase=input("pon tu frase:")
print(frase.upper())
# 17 - Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en minúsculas.
frase=input("pon tu frase:")
print(frase.lower())
# 18 - Crea una variable llamada "frase" y asígnale una cadena de texto de tu elección. Luego, imprime la frase sin espacios en blanco al principio y al final.
frase=" te amo "
print(frase.strip())
# 19 - Crea un código que solicite una frase al usuario y luego imprima la misma frase sin espacios en blanco al principio y al final.
frase=input("pon tu frase:")
print(frase.strip())
# 20 - Crea un código que solicite una frase al usuario y luego imprima la misma frase sin espacios en blanco al principio y al final, además de convertirla a minúsculas.
frase=input("pon tu frase:")
print(frase.strip().upper())
# 21 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las vocales "e" reemplazadas por la letra "f".
frase=input("pon tu frase:")
print(frase.replace("e","f"))
# 22 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las vocales "a" reemplazadas por el carácter "@".
frase=input("pon tu frase:")
print(frase.replace("a","@"))
# 23 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las consonantes "s" reemplazadas por el carácter "$".
frase=input("pon tu frase:")
print(frase.replace("s","$"))