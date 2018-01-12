$(document).ready(function(){
    let colors = true;
    let greys = false;

    $("#colors").click(function(){
        colors = true;
        greys = false;
        $("#grey").attr('checked', false);
        console.log(colors);
        console.log(greys);
        //verander kleuren in colors

    });

    $("#grey").click(function(){
        greys = true;
        colors = false;
        $("#colors").attr('checked', false);
        console.log(colors);
        console.log(greys);
    });

});
