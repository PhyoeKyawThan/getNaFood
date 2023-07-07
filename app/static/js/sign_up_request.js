let datas = {
    username: document.getElementById("username").value,
    email: document.getElementById("email").value,
    password: document.getElementById("password").value
}

let password = document.getElementById("password");
let re_pass = document.getElementById("re-password");
let send = document.getElementById("send");
send.addEventListener("click", ()=>{
    if(password === re_pass){
    const URL = 'auth/sign_up/'
    fetch(URL, {
        method: "POST",
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datas)
    }).then(response => 
            response.json())
    .then(data=>{
        console.log(data)
    }).catch(err=>{
        console.log(err);
    })
}
});