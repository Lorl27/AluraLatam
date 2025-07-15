# Vamos practicar el uso de estructuras condicionales como el if, else y elif a través de algunas actividades. Ahora que estamos avanzando en los contenidos, podemos hacer los desafíos más interesantes: ¡trabajaremos en proyectos de código! Resuelve los problemas iniciales para prepararte para los proyectos:

# Entrenando la programación

# 1 - Escribe un programa que pida a la persona usuaria que proporcione dos números y muestre el número más grande.
from unicodedata import decimal


v1=float(input("1"))
v2=float(input("2"))
if (v1>v2):
    print(v1)
else:
    print(v2)

# 2 - Escribe un programa que solicite el porcentaje de crecimiento de producción de una empresa e informe si hubo un crecimiento (porcentaje positivo) o una disminución (porcentaje negativo).

v2=float(input("% Crec:"))
if (v2>0):
    print("hubo un crecimiento")
else:
    print("Hubo una disminución")

# 3 - Escribe un programa que determine si una letra proporcionada por la persona usuaria es una vocal o una consonante.
v2=input("% Crec:")
if (v2 in ["a","e","i","o","u"]):
    print("vocal")
else:
    print("consonante")
    
# 4 - Escribe un programa que lea valores promedio de precios de un modelo de automóvil durante 3 años consecutivos y muestre el valor más alto y más bajo entre esos tres años.
v1=float(input("p1"))
v2=float(input("p2"))
v3=float(input("p3"))

if(v1>v2 and v1>v3):
    print(f"el valor mas alto es {v1}")
elif(v1<v2 and v2>v3):
    print(f"el valor mas alto es {v2}")
else:
    print(f"el valor mas alto es {v3}")

if(v1>v2 and v3>v2):
    print(f"el valor mas bajo es {v2}")
elif(v1>v3 and v2>v3):
    print(f"el valor mas bajo es {v3}")
else:
    print(f"el valor mas bajo es {v1}")


# 5 - Escribe un programa que pregunte sobre el precio de tres productos e indique cuál es el producto más barato para comprar.

v1=float(input("p1"))
v2=float(input("p2"))
v3=float(input("p3"))

if(v1>v2 and v3>v2):
    print(f"el valor mas bajo es {v2}")
elif(v1>v3 and v2>v3):
    print(f"el valor mas bajo es {v3}")
else:
    print(f"el valor mas bajo es {v1}")

# 6 - Escribe un programa que lea tres números y los muestre en orden descendente.

v1=float(input("p1"))
v2=float(input("p2"))
v3=float(input("p3"))

if(v1>v3>v2):
    print(f"{v1,v3,v2}")
elif(v1>v2>v3):
    print(f"{v1,v2,v3}")
elif(v2>v1>v3):
    print(f"{v2,v1,v3}")
elif(v2>v3>v1):
    print(f"{v2,v3,v1}")
elif(v3>v1>v2):
    print(f"{v3,v1,v2}")
else:
    print(f" {v3,v2,v1}")

# 7 -Escribe un programa que pregunte en qué turno estudia la persona usuaria ("mañana", "tarde" o "noche") y muestre el mensaje "¡Buenos Días!", "¡Buenas Tardes!", "¡Buenas Noches!" o "Valor Inválido!", según el caso.

turno=input("turno:")
if(turno=="mañana"):
    print("Buenos días")
elif(turno=="tarde"):
    print("Buenas tardes")
elif(turno=="noche"):
    print("Buenas noches!")
else:
    print("Valor invalido...")

# 8 - Escribe un programa que solicite un número entero a la persona usuaria y determine si es par o impar. Pista: Puedes usar el operador módulo (%).
nro=int(input("nro:"))
def par(nro):
    if(nro%2==0):
        print("par")
    else:
        print("impar")
        
par(nro)
# 9 - Escribe un programa que pida un número a la persona usuaria y le informe si es entero o decimal.
nro=int(input("nro:"))
def tipo(nro:int):
    if(type(nro)==decimal):
        print("decimal")
    elif(type(nro)==int):
        print("entero")

tipo(nro)
# Momento de los proyectos

# 10 - Un programa debe ser escrito para leer dos números y luego preguntar a la persona usuaria qué operación desea realizar. El resultado de la operación debe incluir información sobre el número, si es par o impar, positivo o negativo, e entero o decimal.

def real(nro):
    if(nro>0):
        print("positivo")
    elif(nro<0):
        print("negativo")
    else:
        print("nulo")

v1=float(input("p1"))
operacion=input("operacion: par - real - tipo")
if(operacion=="par"):
    par(v1)
elif(operacion=="real"):
    real(v1)
else:
    tipo(v1)

# 11 - Escribe un programa que pida a la persona usuaria tres números que representan los lados de un triángulo. El programa debe informar si los valores pueden utilizarse para formar un triángulo y, en caso afirmativo, si es equilátero, isósceles o escaleno. Ten en cuenta algunas sugerencias:

# Tres lados forman un triángulo cuando la suma de cualesquiera dos lados es mayor que el tercero;
# Triángulo Equilátero: tres lados iguales;
# Triángulo Isósceles: dos lados iguales;
# Triángulo Escaleno: tres lados diferentes.

v1=float(input("p1"))
v2=float(input("p2"))
v3=float(input("p3"))

def triangulo(a,b,c):
    if(a+b>c):
        return True
    elif(a+c>b):
        return True
    elif(b+c>a):
        return True
    else:
        return False

if(not triangulo(v1,v2,v3)):
    print("No es...")
else:
    if(v1==v2 or v1==v3 or v2==v3):
        print("T. ISOCELES")
    elif(v1!=v2!=v3):
        print("T. ESCALENO")
    else:
        print("T EQUILATERO")

# 12 - Un establecimiento está vendiendo combustibles con descuentos variables. Para el etanol, si la cantidad comprada es de hasta 15 litros, el descuento será del 2% por litro. En caso contrario, será del 4% por litro. Para el diésel, si la cantidad comprada es de hasta 15 litros, el descuento será del 3% por litro. En caso contrario, será del 5% por litro. El precio por litro de diésel es de R$ 2,00 y el precio por litro de etanol es de R$ 1,70. Escribe un programa que lea la cantidad de litros vendidos y el tipo de combustible (E para etanol y D para diésel) y calcule el valor a pagar por el cliente. Ten en cuenta algunas sugerencias:

# El valor del descuento será el producto del precio por litro, la cantidad de litros y el valor del descuento.
# El valor a pagar por un cliente será el resultado de la multiplicación del precio por litro por la cantidad de litros menos el valor del descuento resultante del cálculo.

# Recolectamos la cantidad de litros y el tipo de combustible,
# convirtiendo el carácter en mayúsculas para facilitar nuestro análisis
cantidad_litros = float(input('Ingrese la cantidad de litros vendidos: '))
tipo_combustible = input('Ingrese el tipo de combustible (E para etanol y D para diésel): ').upper()

# Verificamos primero el tipo de combustible
if tipo_combustible == 'E':
  # Establecemos el precio por litro de etanol
  precio_litro = 1.70
  # Según la cantidad de litros, establecemos el descuento correspondiente
  if cantidad_litros <= 15:
    descuento = 0.02
  else:
    descuento = 0.04
elif tipo_combustible == 'D':
  # Establecemos el precio por litro de diésel
  precio_litro = 2.00
  # Según la cantidad de litros, establecemos el descuento correspondiente
  if cantidad_litros <= 15:
    descuento = 0.03
  else:
    descuento = 0.05
# En caso de error en la especificación del tipo de combustible,
# consideramos las entradas como no válidas y establecemos los precios y descuentos en 0
else:
    print('Entradas no válidas!')
    precio_litro = 0
    descuento = 0

# Calculamos el valor del descuento, seguido del cálculo del precio descontado
valor_descuento = precio_litro * cantidad_litros * descuento
valor_pagado = precio_litro * cantidad_litros - valor_descuento

# Resultado
print(f'Valor a pagar por el cliente: R$ {valor_pagado}')

# 13 - En una empresa de venta de bienes raíces, debes crear un código que analice los datos de ventas anuales para ayudar a la dirección en la toma de decisiones. El código debe recopilar los datos de cantidad de ventas durante los años 2022 y 2023 y calcular la variación porcentual. A partir del valor de la variación, se deben proporcionar las siguientes sugerencias:

# Para una variación superior al 20%: bonificación para el equipo de ventas.
# Para una variación entre el 2% y el 20%: pequeña bonificación para el equipo de ventas.
# Para una variación entre el 2% y el -10%: planificación de políticas de incentivo a las ventas.
# Para bonificaciones inferiores al -10%: recorte de gastos.

# Recolectamos las ventas de los dos años
venta_2022 = float(input('Ingrese la cantidad de ventas en 2022: '))
venta_2023 = float(input('Ingrese la cantidad de ventas en 2023: '))

# Calculamos la variación porcentual entre las ventas de los años 2022 y 2023
var_porcentual = 100 * (venta_2023 - venta_2022) / (venta_2022)

# Análisis condicional de la variación porcentual para determinar la sugerencia a enviar
if var_porcentual > 20:
    print('Bonificación para el equipo de ventas.')
elif 2 <= var_porcentual <= 20:
    print('Pequeña bonificación para el equipo de ventas.')
elif -10 <= var_porcentual < 2:
    print('Planificación de políticas de incentivo a las ventas.')
else:
    print('Recorte de gastos.')