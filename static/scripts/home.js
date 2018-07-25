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
  question_title[i].innerHTML=get_questions[i].innerHTML+".";
}
body.removeChild(document.getElementById("list"));
//changes the input name of all input tags in the question element
//count refers to the number of the question
function change_input_id(array){
  for(let i=1;i<array.length;i++){
    inputs[i].name="q"+count;
  }
}
