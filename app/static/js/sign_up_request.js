let datas = {
    username: document.getElementById("username").value,
    email: document.getElementById("email").value,
    password: document.getElementById("password").value
}

let password = document.getElementById("password");
let re_pass = document.getElementById("re-password");
if(password === re_pass){
    fetch("url_for('auth/sign_up')", {
        method: "POST", 
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datas)
    })
    .then(response => response.json())
    .then(result => {
        console.log()
    })
}