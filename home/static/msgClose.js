const msgBlock = document.getElementById("extra-msg")
const closeMsg = document.getElementById("msg-close")

closeMsg.addEventListener("click", ()=>{
    msgBlock.setAttribute("style", "display: none;")
})