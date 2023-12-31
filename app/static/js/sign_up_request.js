let username = document.getElementById("username");
let email = document.getElementById("email");
let password = document.getElementById("password");

let submit = document.getElementById("send");
let re_pass = document.getElementById("re-password");
let inputs = document.querySelectorAll("input");

inputs.forEach((input)=>{
  input.addEventListener("focus", ()=>{
    document.querySelector(".footer").style.display = "none";
  })
})
submit.addEventListener("click", () => {
  let datas = {
    username: username.value,
    email: email.value,
    password: password.value,
  };
  const URL = "auth/sign_up";
  if (password.value === re_pass.value) {
    fetch(URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(datas),
    })
      .then((response) => {
        if(response.redirected){
            window.location.href = response.url;
        }else{
            return response.json();
        }
      })
      .then((data) => {
        document.querySelector("#alert").textContent = data.message;
      })
      .catch((err) => {
        console.log("Error: ", err);
      });
  } else {
    document.querySelector("#alert").textContent = "Password doesn't Match";
  }
});
