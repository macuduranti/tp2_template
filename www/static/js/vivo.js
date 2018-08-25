$(document).ready(function() {
    start_get_sample();
});

var control_sample;
var interval = 2000;

function start_get_sample() {
    control_sample = setInterval(sample, interval);
}

function stop_get_sample() {
    clearInterval(control_sample);
}

function sample() {
    $.get("/last-sample/", function(data) {
        $("#sid").text(data.id);
        $("#st").text(data.temperature);
        $("#sp").text(data.pressure);
        $("#sh").text(data.humidity);
        $("#sw").text(data.windspeed);
    });
}

$("home-button").click(function() {    
    stop_get_sample();
});

$("#intervalue").addEventListener('input', updateInterval)

function updateInterval(){
    interval = $("#intervalue").val() * 1000;
    stop_get_sample();
    start_get_sample();
}