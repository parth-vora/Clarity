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
  }
}
