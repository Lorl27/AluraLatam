//1. Crea un programa que utilice console.log para mostrar un mensaje de bienvenida.

// 2.Crea una variable llamada "nombre" y asígnale tu nombre. Luego, utiliza console.log para mostrar el mensaje "¡Hola, [tu nombre]!" en la consola del navegador.

// 3.Crea una variable llamada "nombre" y asígnale tu nombre. Luego, utiliza alert para mostrar el mensaje "¡Hola, [tu nombre]!".

// 4.Utiliza prompt y haz la siguiente pregunta: ¿Cuál es el lenguaje de programación que más te gusta?. Luego, almacena la respuesta en una variable y muestra la respuesta en la consola del navegador.

// 5.Crea una variable llamada "valor1" y otra llamada "valor2", asignándoles valores numéricos de tu elección. Luego, realiza la suma de estos dos valores y almacena el resultado en una tercera variable llamada "resultado". Utiliza console.log para mostrar el mensaje "La suma de [valor1] y [valor2] es igual a [resultado]." en la consola.

//6. Crea una variable llamada "valor1" y otra llamada "valor2", asignándoles valores numéricos de tu elección. Luego, realiza la resta de estos dos valores y almacena el resultado en una tercera variable llamada "resultado". Utiliza console.log para mostrar el mensaje "La diferencia entre [valor1] y [valor2] es igual a [resultado]." en la consola.

//7. Pide al usuario que ingrese su edad con prompt. Con base en la edad ingresada, utiliza un if para verificar si la persona es mayor o menor de edad y muestra un mensaje apropiado en la consola.

//8. Crea una variable "numero" y solicita un valor con prompt. Luego, verifica si es positivo, negativo o cero utilizando un if-else y muestra el mensaje correspondiente.

//9. Utiliza un bucle while para mostrar los números del 1 al 10 en la consola.

//10. Crea una variable "nota" y asígnale un valor numérico. Utiliza un if-else para determinar si la nota es mayor o igual a 7 y muestra "Aprobado" o "Reprobado" en la consola.

//1.
console.log("Buenos días");

//2 y 3.
let nombre= "Antonella";
console.log(`¡Hola ${nombre}!`);
alert(`¡Hola ${nombre}!`);

//4. 

let rta= prompt("¿Cuál es el lenguaje de programación que más te gusta?");

console.log(rta);

//5 y 6.

let valor1=15,valor2=2;

let suma=0,resta=0;

suma=valor1+valor2;
resta=valor1-valor2;

let mensaje_1="El resultado de sumar " + valor1 + "con " + valor2 + " es :" + suma;
let mensaje_2=`El resultado de la diferencia entre el ${valor1} y el ${valor2} es ${resta}`;

console.log(mensaje_1,mensaje_2);

//7.

let edad=prompt("Ingrese su edad, porfavor");

edad>=18 ? console.log("Sos mayor de edad!") : console.log("Sos menor de edad.");

//8.

let number = prompt("Ingresa un nro: ");

if(number>0){console.log("Nro positivo.");}
else if(number==0){console.log("Nro constante = 0");}
else{console.log("NRO NEGATIVO");}

//9.
let counter=1;
while(counter<=10){
    console.log(counter);
    counter++;
}

//10.

let nota=8;

nota>=7 ? console.log("Aprobado") : console.log("Reprobado");