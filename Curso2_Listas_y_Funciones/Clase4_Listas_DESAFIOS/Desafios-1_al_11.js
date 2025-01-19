//1. Crea una lista vacía llamada "listaGenerica".
//2. Crea una lista de lenguajes de programación llamada "lenguagesDeProgramacion con los siguientes elementos: 'JavaScript', 'C', 'C++', 'Kotlin' y 'Python'.
//3. Agrega a la lista "lenguagesDeProgramacion los siguientes elementos: 'Java', 'Ruby' y 'GoLang'.
//4. Crea una función que muestre en la consola todos los elementos de la lista "lenguagesDeProgramacion.
//5. Crea una función que muestre en la consola todos los elementos de la lista "lenguagesDeProgramacion en orden inverso.
//6. Crea una función que calcule el promedio de los elementos en una lista de números.
//7. Crea una función que muestre en la consola el número más grande y el número más pequeño en una lista.
//8. Crea una función que devuelva la suma de todos los elementos en una lista.
//9. Crea una función que devuelva la posición en la lista donde se encuentra un elemento pasado como parámetro, o -1 si no existe en la lista.
//10. Crea una función que reciba dos listas de números del mismo tamaño y devuelva una nueva lista con la suma de los elementos uno a uno.
//11. Crea una función que reciba una lista de números y devuelva una nueva lista con el cuadrado de cada número.

//1
let listaGenerica=[];

//2
let lenguagesDeProgramacion=["JavaScript","C","C++","Kotlin","Python"];

//3
lenguagesDeProgramacion.push("Java","Ruby","GoLang");

//4.
function show_list(lista){
    let stop= lista.length;
    
    for(x=0;x<stop;x++){
        console.log(lista[x]);
    }
}

show_list(lenguagesDeProgramacion);

//5
function show_list_Inv(lista){
    
    for(var x=(lista.length-1);x>=0;x--){
        console.log(lista[x]);
    }
}

show_list_Inv(lenguagesDeProgramacion);

//6.

function sumar_numeros(lista){
    let largo=lista.length;
    let cantidad=0;
    for(x=largo-1;x>=0;x--){
        cantidad+=lista[x];
    }
    return cantidad;
}

function prom_list(lista){
    let suma= sumar_numeros(lista);
    let cantidad=lista.length;

    return suma/cantidad;
}

console.log(prom_list([1,2,3]));
console.log(sumar_numeros([1,2,3]));


//7
function maximo_y_minino(lista){
    let maximo=lista[0];
    let minimo=lista[0];

    for(var x=0;x<lista.length;x++){
        if (lista[x]>maximo){
            maximo=lista[x];
        }
        if (lista[x]<minimo){
            minimo=lista[x];
        }
    }

    console.log(`De la lista ${lista}, el nro maximo es: ${maximo} y el minimo: ${minimo}`);
}

maximo_y_minino([1,2,5,0,9,10]);

//8. HECHA EN EL 6

//9.

function positon(lista,elem){
    let largo=lista.length

    if (!lista.includes(elem)){
        return -1;
    }

    for(var x=0;x<largo;x++){
        if(lista[x]==elem){
            return x;
        }
    }
}

console.log(positon([1,4,2,4,7,0],40));

//10.
function conct(l1,l2){
    let largo1=l1.length;
    let largo2=l2.length;
    let max=0,lista=[];
    
    (largo1>largo2) ? max=largo1 : max=largo2;

    for(var x=0;x<max;x++){
        if(x<largo1){lista.push(l1[x])};
        if(x<largo2){lista.push(l2[x])}; //Para que no aparezca "Undefinided".
    }

    return lista;
}

var let1=[1,2,3,5],let2=[6,3,2,0,7,6],let3=[21,22];
console.log(conct(let1,let2));
console.log(conct(let2,let3));

//11.

function cuadrado(lista){
    let largo=lista.length,l=[];

    for(var x=0;x<largo;x++){
        l.push(lista[x]*lista[x]);
    }
    
    return l;
}

console.log(cuadrado([1,2,3,4]));