let num;
let count=0;
for(let i=0; i<5; i++){
    num=parseInt(prompt("Enter a number from 1 to 5"))
    console.log(num)
    count+=num;
    console.log(count)
}
if(count>=5&&count<=11){
  console.log("Tuna")
}else if(count<=12&&count>=18){
  console.log("Fish")
}else{
  console.log("Animal")
}
