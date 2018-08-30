// Ejecuta la función start_get_sample al cargar el documento
$(document).ready(function() {
    start_get_sample();
});

var control_sample;
var interval = 1000; // Por defecto 1 segundo

// Función que comienza el intervalo de muestreo, ejecuta la función sample cada 'interval' milisegundos
function start_get_sample() {
    control_sample = setInterval(sample, interval);
}

// Función que para el intervalo de muestreo
function stop_get_sample() {
    clearInterval(control_sample);
}

// Función sample, se define que se ejecuta cada 'interval' milisegundos
function sample() {
    $.get("/last-sample/", function(data) { // Hace un get en la ruta definida en app.py
        if (data != null) {
            $("#sid").text(data.id);            // Actualiza cada dato en el html
            $("#st").text(data.temperature);
            $("#sp").text(data.pressure);
            $("#sh").text(data.humidity);
            $("#sw").text(data.windspeed);
        }
    });
}

$("home-button").click(function() {    // Al volver al home para el intervalo de meustreo
    stop_get_sample();
});

$("#intervalue")[0].addEventListener('input', updateInterval)  // Al actualizarse el valor del elemento #inervalue, ejecuta la función updateInterval

// Función que actualiza el valor del intervalo de acuerdo al valor en el input
function updateInterval(){
    interval = $("#intervalue").val() * 1000;
    stop_get_sample();
    start_get_sample();
}