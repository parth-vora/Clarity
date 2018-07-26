let total=document.getElementById("total");
let body=document.getElementsByTagName("body")[0];
let div;
let listofoutputs=document.getElementsByClassName("output")

let int=parseInt(total.innerHTML)
// for(let i=0;i<3;i++){
//   console.log(listofoutputs[i].innerHTML);
// }
if(int>=5&&int<=16){
  div=document.createElement("div")
  text=document.createTextNode(listofoutputs[0].innerHTML)
  body.appendChild(div)
  div.appendChild(text)

}else if(int>=17&&int<=28){
  div=document.createElement("div")
  text=document.createTextNode(listofoutputs[1].innerHTML)
  body.appendChild(div)
  div.appendChild(text)
}else{
  div=document.createElement("div")
  text=document.createTextNode(listofoutputs[2].innerHTML)
  body.appendChild(div)
  div.appendChild(text)
}
body.removeChild(document.getElementById("all_outputs"))
