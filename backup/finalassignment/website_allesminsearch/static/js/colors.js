let colorcodes = {

   green : 'rgb(91,185,166)',
   blue : 'rgb(103,198,232)',
   pink : 'rgb(223,40,134)',
   orange : 'rgb(242,143,84)',

}

console.log(document.getElementById('colordata').innerHTML);

if(document.getElementById('colordata').innerHTML == 'c'){

  $("#grey").attr('checked', false);
  $("#colors").attr('checked', true);
  colorcodes.green = 'rgb(91,185,166)';
  colorcodes.blue = 'rgb(103,198,232)';
  colorcodes.pink = 'rgb(223,40,134)';
  colorcodes.orange = 'rgb(242,143,84)';

}else if (document.getElementById('colordata').innerHTML == 'g') {

  $("#colors").attr('checked', false);
  $("#grey").attr('checked', true);
  colorcodes.green = 'rgb(90,97,88)';
  colorcodes.blue = 'rgb(138,149,151)';
  colorcodes.orange = 'rgb(119,120,116)';
  colorcodes.pink = 'rgb(116,110,96)';
}

/*function readColors(){
  console.log(colorcodes);
}
//loop console.log deze dingen
setInterval(readColors, 1000);*/
