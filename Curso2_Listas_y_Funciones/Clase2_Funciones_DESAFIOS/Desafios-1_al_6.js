//1. Crear una función que muestre "¡Hola, mundo!" en la consola.
//2. Crear una función que reciba un nombre como parámetro y muestre "¡Hola, [nombre]!" en la consola.
//3. Crear una función que reciba un número como parámetro y devuelva el doble de ese número.
//4. Crear una función que reciba tres números como parámetros y devuelva su promedio.
//5. Crear una función que reciba dos números como parámetros y devuelva el mayor de ellos.
//6. Crear una función que reciba un número como parámetro y devuelva el resultado de multiplicar ese número por sí mismo.

//1.
function numero1(){
    console.log("¡Hola, mundo!");
}

//2.
function numero2(name){
    console.log(`¡Hola, ${name}!`);
}

//3.
let doble= x => 2*x;

//4
let promedio= (a,b,c) => {return (a+b+c)/3};

//5.
function mayor(a,b){
    return (a>b) ?  a : b;
}

//6.
function multiplicarse(number){
    return number*number;
}

console.log(numero2());
console.log(numero1("Emilio"));
console.log(doble(5));
console.log(promedio(1,2,3));
console.log(mayor(1,2));
console.log(multiplicarse(3));