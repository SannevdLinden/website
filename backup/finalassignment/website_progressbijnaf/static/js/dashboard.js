let heightdiv = $('#goalsbox').height();
//let xhttp = new XMLHttpRequest();

//xhttp.onreadystatechange = function() { // get the user name from a txt file, later this becomes the server
//    if (this.readyState == 4 && this.status == 200) {
//      document.getElementById("username").innerHTML =  //display the username in the first box on the screen
//      this.responseText;
//    }
//  };
//xhttp.open("GET", "info.txt", true);
//xhttp.send();

if ($('#loginbox').height() < 200){ //to make sure all the boxes have at least height 200
    $('#loginbox').height("200px");
}

if ($('#sessionbox').height() < 200){
    $('#sessionbox').height("200px");
}

if ($('#progressbox').height() < 200){
    $('#progressbox').height("200px");
}

if ($('#goalsbox').height() < 200){
    $('#goalsbox').height("200px");
} else { //to make sure all the boxes have the same height to make it more aesthetically pleasing
    $('#loginbox').height(heightdiv) ;
    $('#sessionbox').height(heightdiv);
    $('#progressbox').height(heightdiv);
}

$(window).resize( //if the user resizes the window the boxes need to be resized to
    function(){
        location.reload();
    });


//newnew
let depthprot = 28.0;
let bpprot = 85.0;
let frprot = 20.0;
let speedprot = 120.0;
let ddata;
let bpdata;
let fdata;
let sdata;

ddata = document.getElementsByClassName("data")[0].innerHTML;
ddata = parseFloat(ddata);
console.log(ddata);


bpdata = document.getElementsByClassName("bdata")[0].innerHTML;
bpdata = parseFloat(bpdata);
document.getElementById('bp10value').innerHTML = bpdata;

fdata = document.getElementsByClassName("fdata")[0].innerHTML;
fdata = parseFloat(fdata);

sdata = document.getElementsByClassName("sdata")[0].innerHTML;
sdata = parseFloat(sdata);

if(bpdata-bpprot > 1.0){
  document.getElementById('orangecircle').src= '/static/img/circleorangedecrease.png'
}else if (bpdata-bpprot < -1) {

}else{
  document.getElementById('orangecircle').src= '/static/img/circleorangeconstant.png';
}

if(fdata-frprot > 1.0){

}else if (fdata-frprot < -1) {

}else{

}

if(ddata-depthprot > 1.0){

}else if (ddata-depthprot < -1) {

}else{

}

if(sdata-speedprot > 1.0){

}else if (sdata-speedprot < -1) {

}else{

}
