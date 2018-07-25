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
//Goal: Create all the questionns and puts them in HTML
let element=document.getElementById("question1");
let new_question;
let count=2;
let submit_button=document.getElementById("submit_button");
let last_child;
let inputs;
let get_questions=document.getElementsByClassName("question");
let question_title=document.getElementsByClassName("question_title")
let body=document.getElementsByTagName("body")[0];
for(let i=0;i<get_questions.length;i++){
  console.log(get_questions[i].innerHTML);
}
//let question_list=get_questions.split("\n");
//console.log(question_list);

for(let i=0; i<7; i++){
  //makes a copy of the questions
  new_question=element.cloneNode(true);
  //changes the id of all question so they are unique
  new_question.id="question"+count;
  //returns a string of all children in the question
  inputs=new_question.children;
  //calls the function
  change_input_id(inputs);
  //puts the copied question into HTML
  all_questions.appendChild(new_question);
  count++;
}
for(let i=0; i<8; i++){
  question_title[i].innerHTML=get_questions[i].innerHTML;
}
body.removeChild(document.getElementById("list"));
//changes the input name of all input tags in the question element
//count refers to the number of the question
function change_input_id(array){
  for(let i=1;i<array.length;i++){
    inputs[i].name="q"+count;
>>>>>>> 595116c8085111e47dd7f34c271f77d9f30f6642
  }
}
