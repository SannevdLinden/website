let flowdata = []; //data for the 4 graph lines
let bloodpressuredata = [];
let depthdata = [];
let speeddata = [];
let emptyarray = []; //empty array when the data is not displayed
let ctx; //the canvas element
let bloodpressure = false; //booleans is the grpah lines are displayed or not
let flowrate = false;
let depth = false;
let speed = false;
let datastr1 = []; // load in the data in this empty array from txt files
let datastr2 = [];
let datastr3 = [];
let datastr4 = [];
let xhttp = new XMLHttpRequest(); //request the data for all the graphs from the server, this will become a database
let xhttp2 = new XMLHttpRequest();
let xhttp3 = new XMLHttpRequest();
let xhttp4 = new XMLHttpRequest();
var databp;

xhttp.onreadystatechange = function() { //gets the data from the txt file
    if (this.readyState == 4 && this.status == 200) {
      datastr1 = this.responseText;
    }
};
xhttp.open("GET", "bpdata.txt", true);
xhttp.send();

xhttp2.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      datastr2 = this.responseText;
    }
};
xhttp2.open("GET", "frdata.txt", true);
xhttp2.send();

xhttp3.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      datastr3 = this.responseText;
    }
};
xhttp3.open("GET", "ddata.txt", true);
xhttp3.send();

xhttp4.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      datastr4 = this.responseText;
    }
};
xhttp4.open("GET", "sdata.txt", true);
xhttp4.send();


setTimeout(function(){ //data needs a moment to load, therefore wait a bit.  

    bloodpressuredata = datastr1.split(","); //the data is loaded in the form of a string need to be splitted
    flowdata = datastr2.split(",");
    depthdata = datastr3.split(",");
    speeddata = datastr4.split(",");

}, 100);

let config = { //configuration for the graph
    type: 'line',
    data: {
        labels: ["1", "2", "3", "4", "5"], //labels x-axis
        datasets: [{ //all the different lines
            label: "Blood pressure",
            backgroundColor: 'rgb(242,143,84)',
            borderColor: 'rgb(242,143,84)',
            data: emptyarray, //data loaded in the graph
            fill: false,
        }, {
            label: "Flow rate",
            fill: false,
            backgroundColor: 'rgb(223,40,134)',
            borderColor: 'rgb(223,40,134)',
            data: emptyarray,
        },
                  {
            label: "Depth",
            fill: false,
            backgroundColor: 'rgb(103,198,232)',
            borderColor: 'rgb(103,198,232)',
            data: emptyarray,
        },
           {
            label: "Speed",
            fill: false,
            backgroundColor: 'rgb(91,185,166)',
            borderColor: 'rgb(91,185,166)',
            data: emptyarray,
           }]
    },
    options: { //options for displaying the box with the exact values, when hover over the graph
        responsive: true,
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        hover: { 
            mode: 'nearest',
            intersect: true
        },
        scales: { //config for the axis
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Session Number'
                }                        
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Value'
                },
                ticks: {
                        beginAtZero: true,
                        max: 150
                    }
            }]
        }
    }
};
        
$(window).load(function() {
    ctx = document.getElementById("canvas").getContext("2d"); //draw the graph
    window.myLine = new Chart(ctx, config);
});


$('#bpline').click(function() {
  if (bloodpressure == true){ //hide the bp line
      config.data.datasets[0].data = emptyarray; // load empty array in graph
      document.getElementById("bpline").innerHTML = "show blood pressure"; //change text on button
      bloodpressure = false;
  } else if (bloodpressure == false) { //show the bpline
      config.data.datasets[0].data = bloodpressuredata;
      document.getElementById("bpline").innerHTML = "hide blood pressure";
      bloodpressure = true;
  } else{
      console.log("something went wrong");
  }          
  window.myLine.update(); //load the changes in graph
});


$('#frline').click(function() { //show/hide flow rate data
     if (flowrate == true){
      config.data.datasets[1].data = emptyarray;
      document.getElementById("frline").innerHTML = "show flow rate";
      flowrate = false;
  } else if (flowrate == false) {
      config.data.datasets[1].data = flowdata;
      document.getElementById("frline").innerHTML = "hide flow rate";
      flowrate = true;
  } else{
      console.log("something went wrong");
  }          
  window.myLine.update(); 
});

$('#dline').click(function() { //show/hide depth data
     if (depth == true){
      config.data.datasets[2].data = emptyarray;
      document.getElementById("dline").innerHTML = "show depth";
      depth = false;
  } else if (depth == false) {
      config.data.datasets[2].data = depthdata;
      document.getElementById("dline").innerHTML = "hide depth";
      depth = true;
  } else{
      console.log("something went wrong");
  }          
  window.myLine.update(); 
});

$('#sline').click(function() { //show/hide speed data
     if (speed == true){
      config.data.datasets[3].data = emptyarray;
      document.getElementById("sline").innerHTML = "show speed";
      speed = false;
  } else if (speed == false) {
      config.data.datasets[3].data = speeddata;
      document.getElementById("sline").innerHTML = "hide speed";
      speed = true;
  } else{
      console.log("something went wrong");
  }          
  window.myLine.update(); 
});