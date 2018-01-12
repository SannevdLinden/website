$(document).ready(function(){
    let arrowq1 = false;
    let arrowq2 = false;
    let arrowq3 = false;

    $("#titleq1").click(function(){
        $("#ansq1").toggle();
        if (arrowq1 == false){
          arrowq1 = true;
          document.getElementById("arrowq1").innerHTML = "&#9650;";
        }else{
          arrowq1 = false;
            document.getElementById("arrowq1").innerHTML = "&#9660;";
        }
    });
    $("#titleq2").click(function(){
        $("#ansq2").toggle();
        if (arrowq2 == false){
          arrowq2 = true;
          document.getElementById("arrowq2").innerHTML = "&#9650;";
        }else{
          arrowq2 = false;
          document.getElementById("arrowq2").innerHTML = "&#9660;";
        }
    });
    $("#titleq3").click(function(){
        $("#ansq3").toggle();
        if (arrowq3 == false){
          arrowq3 = true;
          document.getElementById("arrowq3").innerHTML = "&#9650;";
        }else{
          arrowq3 = false;
          document.getElementById("arrowq3").innerHTML = "&#9660;";
        }
    });

    $("#titleq1").css("background-color", colorcodes.green);
    $("#titleq3").css("background-color", colorcodes.green);
    $(".contactformbutton").css("background-color", colorcodes.green);


});
