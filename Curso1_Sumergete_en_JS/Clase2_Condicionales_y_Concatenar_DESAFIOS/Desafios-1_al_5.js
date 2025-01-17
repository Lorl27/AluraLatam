// 1.Pregunta al usuario qué día de la semana es. Si la respuesta es "Sábado" o "Domingo", muestra "¡Buen fin de semana!". De lo contrario, muestra "¡Buena semana!".

// 2.Verifica si un número ingresado por el usuario es positivo o negativo. Muestra una alerta informativa.

// 3.Crea un sistema de puntuación para un juego. Si la puntuación es mayor o igual a 100, muestra "¡Felicidades, has ganado!". En caso contrario, muestra "Intentalo nuevamente para ganar.".

// 4.Crea un mensaje que informe al usuario sobre el saldo de su cuenta, utilizando un template string para incluir el valor del saldo.

// 5.Pide al usuario que ingrese su nombre mediante un prompt. Luego, muestra una alerta de bienvenida usando ese nombre.

//1
const msg= "¡Buen fin de semana!";
const mensaje="¡Buena semana!";

let rta=prompt("¿Qué día de la semana es?");

if(rta=="domingo" || rta=="sábado"){
    alert(msg);
}
else{
    alert(mensaje);
}

//2

let usr= prompt("Ingrese un nro:");
if(usr<0){
    alert("Usted ha ingresado un nro negativo");
}
else if(usr>0){
    alert("Usted ha ingresado un nro positivo");
}
else{ alert("Usted ingreso el 0");}

//3.
let puntuacion=prompt("Ingrese la puntuación");

if(puntuacion>=100){ alert("¡Felicidades, has ganado");}
else{
    alert("Intentalo nuevamente para ganar.");
}

//4.

let saldoDeLaCuenta=5030;

alert(`Su saldo es de ${saldoDeLaCuenta}`);

//5.
let name=prompt("Ingrese su nombre: ");
let msj=`Bienvenid@ , ${name}!`;

alert(msj);