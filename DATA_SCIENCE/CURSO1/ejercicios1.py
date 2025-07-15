# Vamos a practicar el uso de la función print con algunas actividades. Para ello, resuelve los problemas propuestos en código:

# 1 - Imprime la frase "Escuela de Datos de Alura".

print("Escuela de Datos de Alura")
# 2 - Imprime tu nombre y tu apellido siguiendo la estructura a continuación:
#     Nombre: [tu nombre]
#     Apellido: [tu apellido]
    
print(""" Nombre: Antonella , Apellido: Grassi """)

# 3 - Imprime tu primer nombre letra por letra. Por ejemplo, si mi nombre es Álvaro, la salida sería:
    
for x in "Antonella":
    print(x)
    
# 4 - Imprime tu fecha de nacimiento en formato día mes año. Recuerda que los valores de día y año no deben estar entre comillas. Suponiendo una fecha de cumpleaños el 28 de febrero de 2003, el formato debe ser como el siguiente:
#     28 febrero 2003
    
cumple=[27,"julio",2004]
print(cumple[0],cumple[1],cumple[2])

# 5 - Imprime, en una sola instrucción print, el año actual en el que estás realizando este curso. El valor del año debe ser un dato numérico, y la salida de print debe ser la siguiente:
#     Año actual: [año]
    
print(f"Año actual: {2025}")