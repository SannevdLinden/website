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
    document.getElementById('d10value').innerHTML = ddata;

    bpdata = document.getElementsByClassName("bdata")[0].innerHTML;
    bpdata = parseFloat(bpdata);
    document.getElementById('bp10value').innerHTML = bpdata;

    fdata = document.getElementsByClassName("fdata")[0].innerHTML;
    fdata = parseFloat(fdata);
    document.getElementById('fr10value').innerHTML = fdata;

    sdata = document.getElementsByClassName("sdata")[0].innerHTML;
    sdata = parseFloat(sdata);
    document.getElementById('s10value').innerHTML = sdata;

    if(bpdata-bpprot > 1.0){
      document.getElementById('orangecircle').src= '/static/img/circleorangedecrease.png';
    }else if (bpdata-bpprot < -1) {
      document.getElementById('orangecircle').src= '/static/img/circleorangeprogress.png';
    }else{
      document.getElementById('orangecircle').src= '/static/img/circleorangeconstant.png';
    }

    if(document.getElementById('colordata').innerHTML == 'g'){
      if(bpdata-bpprot > 1.0){
        document.getElementById('orangecircle').src= '/static/img/circleorangedecreasegrey.png';
      }else if (bpdata-bpprot < -1) {
        document.getElementById('orangecircle').src= '/static/img/circleorangeprogressgrey.png';
      }else{
        document.getElementById('orangecircle').src= '/static/img/circleorangeconstantgrey.png';
      }
    }

    if(fdata-frprot > 1.0){
      document.getElementById('pinkcircle').src= '/static/img/circlepinkdecrease.png';
    }else if (fdata-frprot < -1) {
      document.getElementById('pinkcircle').src= '/static/img/circlepinkprogress.png';
    }else{
      document.getElementById('pinkcircle').src= '/static/img/circlepinkconstant.png';
    }

    if(document.getElementById('colordata').innerHTML == 'g'){
      if(fdata-frprot > 1.0){
        document.getElementById('pinkcircle').src= '/static/img/circlepinkdecreasegrey.png';
      }else if (fdata-frprot < -1) {
        document.getElementById('pinkcircle').src= '/static/img/circlepinkprogressgrey.png';
      }else{
        document.getElementById('pinkcircle').src= '/static/img/circlepinkconstantgrey.png';
      }
    }

    if(ddata-depthprot > 1.0){
      document.getElementById('bluecircle').src= '/static/img/circlebluedecrease.png';
    }else if (ddata-depthprot < -1) {
      document.getElementById('bluecircle').src= '/static/img/circleblueprogress.png';
    }else{
      document.getElementById('bluecircle').src= '/static/img/circleblueconstant.png';
    }

    if(document.getElementById('colordata').innerHTML == 'g'){
      if(ddata-depthprot > 1.0){
        document.getElementById('bluecircle').src= '/static/img/circlebluedecreasegrey.png';
      }else if (ddata-depthprot < -1) {
        document.getElementById('bluecircle').src= '/static/img/circleblueprogressgrey.png';
      }else{
        document.getElementById('bluecircle').src= '/static/img/circleblueconstantgrey.png';
      }
    }

    if(sdata-speedprot > 1.0){
      document.getElementById('greencircle').src= '/static/img/circlegreendecrease.png';
    }else if (sdata-speedprot < -1) {
      document.getElementById('greencircle').src= '/static/img/circlegreenprogress.png';
    }else{
      document.getElementById('greencircle').src= '/static/img/circlegreenconstant.png';
    }

    if(document.getElementById('colordata').innerHTML == 'g'){
      if(sdata-speedprot > 1.0){
        document.getElementById('greencircle').src= '/static/img/circlegreendecreasegrey.png';
      }else if (sdata-speedprot < -1) {
        document.getElementById('greencircle').src= '/static/img/circlegreenprogressgrey.png';
      }else{
        document.getElementById('greencircle').src= '/static/img/circlegreenconstantgrey.png';
      }
    }



    $("#loginbox").css("background-color", colorcodes.blue);
    $("#goalsbox").css("background-color", colorcodes.blue);
