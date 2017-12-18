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
