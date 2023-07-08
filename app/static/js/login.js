document.querySelector("button").addEventListener("click", ()=>{
    let datas = {
        username: "domak", 
        password: "pass"
    }
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
          console.log(data);
        })
        .catch((err) => {
          console.log("Error: ", err);
        });
})