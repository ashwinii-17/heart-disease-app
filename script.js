let step = 0

function showStep(){

let steps = document.querySelectorAll(".step")

steps.forEach((s,i)=>{
s.classList.remove("active")

if(i === step){
s.classList.add("active")
}

})

}

function nextStep(){

let steps = document.querySelectorAll(".step")

if(step < steps.length-1){
step++
showStep()
}

}

function prevStep(){

if(step>0){
step--
showStep()
}

}