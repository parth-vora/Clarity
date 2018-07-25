<<<<<<< HEAD
var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
// Create a "close" button and append it to each list item
var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(span);
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}

// Add a "checked" symbol when clicking on a list item
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');
  }
}, false);

// Create a new list item when clicking on the "Add" button
function newElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("myInput").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("You must write something!");
  } else {
    document.getElementById("myUL").appendChild(li);
  }
  document.getElementById("myInput").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
=======
// let num;
// let count=0;
// for(let i=0; i<5; i++){
//     //num=parseInt(prompt("Enter a number from 1 to 5"))
//     console.log(num);
//     count+=num;
//     console.log(count);
// }
// if(count>=5&&count<=11){
//   console.log("Tuna")
// }else if(count>=12&&count<=18){
//   console.log("Fish");
// }else{
//   console.log("Animal");
// }
console.log("njkfdn")
let element=document.getElementById("question1");
let new_question;
let count=2;
let submit_button=document.getElementById("submit_button");
let question_title;
let last_child;
let inputs;
for(let i=0; i<7; i++){
  //makes a copy of the questions
  new_question=element.cloneNode(true);
  //changes the id of all question so they are unique
  new_question.id="question"+count;
  //returns a string of all children in the question
  inputs=new_question.children;
  change_input_id(inputs);
  all_questions.appendChild(new_question);
  console.log(new_question.id);
  count++;
}
function change_input_id(array){
  for(let i=1;i<array.length;i++){
    inputs[i].name="q"+count;
>>>>>>> 9f755e8ae4e24d345821cbaefff1fa2082f35bb8
  }
}
