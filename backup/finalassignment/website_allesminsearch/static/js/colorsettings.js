$(document).ready(function(){
    if(document.getElementById('colordata').innerHTML == 'c'){
    let colors = true;
    let greys = false;
    $("#grey").attr('checked', false);
    $("#colors").attr('checked', true);
    colorcodes.green = 'rgb(91,185,166)';
    colorcodes.blue = 'rgb(103,198,232)';
    colorcodes.pink = 'rgb(223,40,134)';
    colorcodes.orange = 'rgb(242,143,84)';
  }else if (document.getElementById('colordata').innerHTML == 'g') {
    let colors = false;
    let greys = true;
    $("#colors").attr('checked', false);
    $("#grey").attr('checked', true);
    colorcodes.green = 'rgb(90,97,88)';
    colorcodes.blue = 'rgb(138,149,151)';
    colorcodes.orange = 'rgb(119,120,116)';
    colorcodes.pink = 'rgb(116,110,96)';
  }


    $("#colors").click(function(){
        colors = true;
        greys = false;
        $("#grey").attr('checked', false);
        console.log(colors);
        console.log(greys);
        //change colors in colors.js
        if (colors == true){
          colorcodes.green = 'rgb(91,185,166)';
          colorcodes.blue = 'rgb(103,198,232)';
          colorcodes.pink = 'rgb(223,40,134)';
          colorcodes.orange = 'rgb(242,143,84)';
          //console.log("test" + colorcodes.green);
        }

    });

    $("#grey").click(function(){
        greys = true;
        colors = false;
        $("#colors").attr('checked', false);
        console.log(colors);
        console.log(greys);
        if (greys == true){
          colorcodes.green = 'rgb(90,97,88)';
          colorcodes.blue = 'rgb(138,149,151)';
          colorcodes.orange = 'rgb(119,120,116)';
          colorcodes.pink = 'rgb(116,110,96)';
        }
       //console.log("test2" + colorcodes.green);
    });

});
