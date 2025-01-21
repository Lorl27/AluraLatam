let titulo= document.querySelector("h1");
titulo.innerHTML= "Hora del desafío";

function mensaje_console(){
    console.log("El botón fue apretado.");
}

function mensaje_prompt(){
    let usr=prompt("Dame una ciudad de Brasil: ");
    alert(`Estuve en ${usr}`);
}

function mensaje_alert(){
    alert("Yo amo JS");
}

function mensaje_suma(){
    let numero1= parseInt(prompt("Ingrese un nro: "));

    let numero2= parseInt(prompt("Ingrese otro nro: "));

    alert(`El resultado de sumar ${numero1} con ${numero2} es: ${numero1+numero2}`);
}