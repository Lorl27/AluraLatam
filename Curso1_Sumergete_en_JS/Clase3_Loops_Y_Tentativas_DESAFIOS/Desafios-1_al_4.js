// 1.Crea un contador que comience en 1 y vaya hasta 10 usando un bucle 'while'. Muestra cada número.
// 2.Crea un contador que comience en 10 y vaya hasta 0 usando un bucle 'while'. Muestra cada número.
// 3.Crea un programa de cuenta regresiva. Pide un número y cuenta desde ese número hasta ese 0 utilizando un bucle 'while' en la consola del navegador.
// 4.Crea un programa de cuenta progresiva. Pide un número y cuenta desde 0 hasta ese número utilizando un bucle 'while' en la consola del navegador.

let contador_1=1,contador_2=10,contador_3,contador_4;

//1
while(contador_1<=10){
    console.log(contador_1);
    contador_1+=1;
}

//2:
while(contador_2>=0){
    console.log(contador_2);
    contador_2-=1;
}

//3:
contador_3=prompt("Elige un nro: ");
while(contador_3>=0){
    console.log(contador_3);
    contador_3--;
}

//4:
contador_4=prompt("Dame otro:");
let start=0;
while(start<contador_4){
    console.log(start);
    start++;
}

