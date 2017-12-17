//this is based on an example from w3schools, https://www.w3schools.com/howto/howto_js_todolist.asp

let myNodelist = document.getElementById("myUL").getElementsByTagName("LI"); // all items in list of to do's
let myNodelistcomplete = document.getElementById("myULcomplete").getElementsByTagName("LI"); //all items in list completed to do's
let close = document.getElementsByClassName("close"); //for deleting an element
let list = document.getElementById("myUL");
let completedtasks = document.getElementById("myULcomplete");
let i; //variables for counting
let j;
let q;
let longestword = 0; //longest word in the input

// Create a "close" button and append it to each list item
for (i = 0; i < myNodelist.length; i++) {
  let span = document.createElement("button");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(span);
}

// Create a "close" button and append it to each list item completed
for (q = 0; q < myNodelistcomplete.length; q++) {
  let span = document.createElement("button");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelistcomplete[q].appendChild(span);
}

// Click on a close button to hide the current list item
for (j = 0; j < close.length; j++) {
  close[j].onclick = function() {
    let div = this.parentElement;
    div.style.display = "none";
  }
}

// Add a "checked" symbol when clicking on a list item
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');


    //if checked move to other list
    if(ev.target.classList == "checked"){
         completedtasks.appendChild(ev.target);       
     }
  }
}, false);


// Add a "checked" symbol when clicking on a list item
completedtasks.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');
    //if not checked move back
    if(ev.target.classList == ""){
       list.appendChild(ev.target);
    }
  }
}, false);


function longestwordinstring(str){ //find the longest word in the input
    let split = str.split(' ');
    let p;

    for(p = 0; p < split.length; p++){
        if(split[p].length > longestword){
	       longestword = split[p].length;
        }
    }
}


// Create a new list item when clicking on the "Add" button
function newElement() {
  let li = document.createElement("li");
  let inputValue = document.getElementById("input").value;
  let t = document.createTextNode(inputValue);
  let span = document.createElement("SPAN");
  let txt = document.createTextNode("\u00D7");
  let k;
  let div;

  longestwordinstring(inputValue); //search for the longest word

  li.appendChild(t);
  if (inputValue === '') {
    alert("Please write something!");
  } else if (longestword > 15){
      alert("Words over 15 characters are not supported"); //not allowed to have words longer than 15 characters
      longestword = 0;
  } else {
    document.getElementById("myUL").appendChild(li);
  }
  document.getElementById("input").value = "";

  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (k = 0; k < close.length; k++) {
    close[k].onclick = function() {
      div = this.parentElement;
      div.style.display = "none";
    }
  }
}
