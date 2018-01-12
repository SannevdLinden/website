let flowdata = [0,0,0,0,0,0,0,0,0,0]; //data for the 4 graph lines
let bloodpressuredata = [0,0,0,0,0,0,0,0,0,0];
let depthdata = [0,0,0,0,0,0,0,0,0,0];
let speeddata = [0,0,0,0,0,0,0,0,0,0];

let emptyarray = []; //empty array when the data is not displayed
let ctx; //the canvas element
let bloodpressure = true; //booleans is the grpah lines are displayed or not
let flowrate = true;
let depth = true;
let speed = true;
let datastr1 = []; // load in the data in this empty array from txt files
let datastr2 = [];
let datastr3 = [];
let datastr4 = [];
let xhttp = new XMLHttpRequest(); //request the data for all the graphs from the server, this will become a database
let xhttp2 = new XMLHttpRequest();
let xhttp3 = new XMLHttpRequest();
let xhttp4 = new XMLHttpRequest();

//NEWNEW
let databp;
let bpdata;
let fdata;
let sdata;
let depthprot = 28.0;
let bpprot = 85.0;
let frprot = 20.0;
let speedprot = 120.0;
let heightdiv = $('#bpprogress').height();

$('#frprogress').height(heightdiv) ;
$('#dprogress').height(heightdiv);
$('#sprogress').height(heightdiv);

$("#bpline").css("background-color", colorcodes.orange);
$("#frline").css("background-color", colorcodes.pink);
$("#dline").css("background-color", colorcodes.blue);
$("#sline").css("background-color", colorcodes.green);


$("#bpprogress").css("background-color", colorcodes.orange);
$("#frprogress").css("background-color", colorcodes.pink);
$("#dprogress").css("background-color", colorcodes.blue);
$("#sprogress").css("background-color", colorcodes.green);

$(window).resize( //if the user resizes the window the boxes need to be resized to
    function(){
        location.reload();
    });

for (i=0; i<10; i++){
  ddata = document.getElementsByClassName("data")[i].innerHTML;
  ddata = parseFloat(ddata);
  depthdata[i] =ddata;
}
console.log(depthdata);

for (i=0; i<10; i++){
  bpdata = document.getElementsByClassName("bdata")[i].innerHTML;
  bpdata = parseFloat(bpdata);
  bloodpressuredata[i] =bpdata;
}
console.log(bloodpressuredata);

for (i=0; i<10; i++){
  fdata = document.getElementsByClassName("fdata")[i].innerHTML;
  fdata = parseFloat(fdata);
  flowdata[i] =fdata;
}
console.log(flowdata);

for (i=0; i<10; i++){
  sdata = document.getElementsByClassName("sdata")[i].innerHTML;
  sdata = parseFloat(sdata);
  speeddata[i] =sdata;
}
console.log(speeddata);

if(bloodpressuredata[9]-bpprot > 1.0){
  document.getElementById("bpprogresstext").innerHTML = "Your blood pressure value is too high, try to reach the optimal of 85.0 systolic pressure.";
  //console.log(document.getElementById("bpprogresstext").innerHTML);
}else if (bloodpressuredata[9]-bpprot < -1) {
  document.getElementById("bpprogresstext").innerHTML = "Your blood pressure value is too low, try to reach the optimal of 85.0 systolic pressure.";
}else{
  document.getElementById("bpprogresstext").innerHTML = "Keep up the good work! You succeeded to reach the optimal of 85.0 systolic pressure.";
}

if(flowdata[9]-frprot > 1.0){
  document.getElementById("frprogresstext").innerHTML = "Your flow rate value is too high, try to reach the optimal of 20.0 ml/min.";
  //console.log(document.getElementById("frprogresstext").innerHTML);
}else if (flowdata[9]-frprot < -1) {
  document.getElementById("frprogresstext").innerHTML = "Your flow rate value is too low, try to reach the optimal of 20.0 ml/min.";
}else{
  document.getElementById("frprogresstext").innerHTML = "Keep up the good work! You succeeded to reach the optimal of 20.0 ml/min.";
}

if(depthdata[9]-depthprot > 1.0){
  document.getElementById("dprogresstext").innerHTML = "Your depth value is too high, try to reach the optimal of 28.0 mm.";
  //console.log(document.getElementById("dprogresstext").innerHTML);
}else if (depthdata[9]-depthprot < -1) {
  document.getElementById("dprogresstext").innerHTML = "Your depth value is too low, try to reach the optimal of 28.0 mm.";
}else{
  document.getElementById("dprogresstext").innerHTML = "Keep up the good work! You succeeded to reach the optimal of 28.0 mm.";
}

if(speeddata[9]-speedprot > 1.0){
  document.getElementById("sprogresstext").innerHTML = "Your speed value is too high, try to reach the optimal of 120.0 bpm.";
  //console.log(document.getElementById("bpprogresstext").innerHTML);
}else if (speeddata[9]-speedprot < -1) {
  document.getElementById("sprogresstext").innerHTML = "Your speed value is too low, try to reach the optimal of 120.0 bpm.";
}else{
  document.getElementById("sprogresstext").innerHTML = "Keep up the good work! You succeeded to reach the optimal of 120.0 bpm.";
}


/*xhttp.onreadystatechange = function() { //gets the data from the txt file
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
*/

let config = { //configuration for the graph
    type: 'line',
    data: {
        labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], //labels x-axis
        datasets: [{ //all the different lines
            label: "Blood pressure (systolic)",
            backgroundColor: colorcodes.orange,
            borderColor: colorcodes.orange,
            data: bloodpressuredata, //data loaded in the graph
            fill: false,
        }, {
            label: "Flow rate (ml/min)",
            fill: false,
            backgroundColor: colorcodes.pink,
            borderColor: colorcodes.pink,
            data: flowdata,
        },
                  {
            label: "Depth (mm)",
            fill: false,
            backgroundColor: colorcodes.blue,
            borderColor: colorcodes.blue,
            data: depthdata,
        },
           {
            label: "Speed (bpm)",
            fill: false,
            backgroundColor: colorcodes.green,
            borderColor: colorcodes.green,
            data: speeddata,
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
