let username = document.querySelector("input[type='text']");
let password = document.querySelector("input[type='password']");
let inputs = document.querySelectorAll("input");

inputs.forEach((input)=>{
  input.addEventListener("focus", ()=>{
    document.querySelector(".footer").style.display = "none";
  })
})

document.querySelector("#button").addEventListener("click", ()=>{
    let datas = {
        username: username.value,
        password: password.value
    }
  if(datas.username != "" && datas.password != ""){
    const URL = "auth/login"
    fetch(URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(datas),
      })
        .then((response) => {
            if (response.redirected){
                window.location.href = response.url;
            }else{
                return response.json();
            }
        })
        .then((data) => {
          document.querySelector("span").textContent = data.message;
        })
        .catch((err) => {
          console.log("Error: ", err);
        });
      }else{
        document.querySelector("span").textContent = "Username and password musn't be emply";
      }
})