let titulo= document.querySelector("h1");
titulo.innerHTML= "This is a tittle";

/**
 *  function asignarHTML(elemento,string){
        document.queriSelector(elemento).innerHTML=string;}
**/

/* HTML :
<meta code>
<head>
<script src="file.js"> </script>
</head> 

<body>

<h1> </h1>
<p class="parrafo"> </p>

<input type="number" id="id_input"> </input>

<button class="button_syle" onclick="inicar_game();" disabled> Iniciar juego </button>
</body>
*/

function inicar_game(){
    //do something
}

let ingresoInput= document.getElementById("id_input").value;

let vaciarINPUT = document.querySelector("#id_input").value=""; //== document.getElementById("id_input")

let reinicarGame=document.querySelector("#id_input").removeAttribute("disabled");

document.getElementById("id_input").setAttribute("disabled","true");

//-----------------------------------
let celsiusAFahrenheit = celsius => (celsius * 9/5) + 32; //función flecha 
let mayor = (a, b) => (a > b ? a : b); //f. flecha