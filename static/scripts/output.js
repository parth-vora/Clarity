let total=document.getElementById("total");
let body=document.getElementsByTagName("body")[0];
let div;
let listofoutputs=["Good Luck","Mehhh","Great"]
let int=parseInt(total.innerHTML)
if(int>=5&&int<=11){
  div=document.createElement("div")
  text=document.createTextNode(listofoutputs[0])
  body.appendChild(div)
  div.appendChild(text)

}else if(int>=12&&int<=18){
  div=document.createElement("div")
  text=document.createTextNode(listofoutputs[1])
  document.appendChild(div)
  div.appendChild(text)
}else{
  div=document.createElement("div")
  text=document.createTextNode(listofoutputs[2])
  body.appendChild(div)
  div.appendChild(text)
}
