const submitBtn = document.getElementById("submit-btn")
const form = document.getElementById("book-form")
const mobileField = document.getElementById("mobile")
const errorMessage = document.getElementById("error")

submitBtn.addEventListener("click", (event)=>{
    event.preventDefault()
    let valid = true
    let mobile = mobileField.value.toString()
    if(mobile.length!=10){
        errorMessage.textContent = "Please enter your valid 10 digit mobile number"
        errorMessage.setAttribute("style", "display: block;")
        valid = false
    }
    if(!form.checkValidity()){
        form.reportValidity()
    }

    else if(valid && form.checkValidity()){
        console.log(valid)
        form.noValidate = false
        form.submit()
    }
})