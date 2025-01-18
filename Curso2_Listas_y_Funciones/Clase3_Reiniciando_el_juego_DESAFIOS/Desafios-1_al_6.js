//1. Crea una función que calcule el índice de masa corporal (IMC) de una persona a partir de su altura en metros y peso en kilogramos, que se recibirán como parámetros.
//2. Crea una función que calcule el valor del factorial de un número pasado como parámetro.
//3. Crea una función que convierta un valor en dólares, pasado como parámetro, y devuelva el valor equivalente en reales(moneda brasileña,si deseas puedes hacerlo con el valor del dólar en tu país). Para esto, considera la cotización del dólar igual a R$4,80.
//4. Crea una función que muestre en pantalla el área y el perímetro de una sala rectangular, utilizando la altura y la anchura que se proporcionarán como parámetros.
//5. Crea una función que muestre en pantalla el área y el perímetro de una sala circular, utilizando su radio que se proporcionará como parámetro. Considera Pi = 3,14.
//6. Crea una función que muestre en pantalla la tabla de multiplicar de un número dado como parámetro.

//1

function redondear_decimales(calculo){
    return Math.ceil(calculo*100)/100;
}

function calcular_IMC(altura,peso){
    let calculo=peso/(altura*altura);
    return redondear_decimales(calculo);
}

//2
function factorial(numero){
    let fact=1;

    if (numero==1 || numero==0){
    return fact;}

    return numero  * (factorial(numero-1));
}

console.log(factorial(5));

//3
function pesosToDolar(pesos){
    return pesos * 0.00096;
}

console.log(pesosToDolar(10000));

//4
function calcular_Area_y_Perimetro(alto,ancho){
    let resultado_Area= alto*ancho;
    let resultado_Perimetro= 2*(alto+ancho);

    console.log(`El área de la sala rectangular de ${alto}x${ancho}cm es: ${resultado_Area}cm ${ resultado_Area==1 ? "cuadrado" : "cuadrados"} y su perimetro es: ${resultado_Perimetro}cm`);
}

calcular_Area_y_Perimetro(3,5);

console.log(calcular_IMC(1.66,57));

//5 

function calcular_Area_y_Perimetro_2(radio){
    let resultado_Area= Math.PI*radio*radio;
    let resultado_Perimetro= 2*radio*Math.PI;

    console.log(`El área de la sala circular es: ${redondear_decimales(resultado_Area)}cm ${ resultado_Area==1 ? "cuadrado" : "cuadrados"} y su perimetro es: ${redondear_decimales(resultado_Perimetro)}cm`);
}

calcular_Area_y_Perimetro_2(5);

//6

function tabla(numero){
    let contador=0;
    while(contador<=10){
        console.log(contador*numero);
        contador++;
    }
}

tabla(3);