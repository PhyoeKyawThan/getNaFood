let add_cart = document.querySelectorAll(".add");
let success = document.querySelector(".success");

add_cart.forEach(add => {
    add.addEventListener("click", (e)=>{
        let count = Number(prompt("Enter amount of items Number Only"));
        if(count){
            const URL = "/add_cart";
            let request = {
                count: count,
                order_id: e.target.id
            }
            fetch(URL, {
                method: "POST",
                headers:{
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(request)
            }).then(response=>{
                if(response.redirected){
                    window.location.href = response.url;
                }else{
                    return response.json();
                }
            })
            .then(datas => {
                success.style.display = 'block';
                success.innerText = datas.message;
                setTimeout(()=>{
                    success.style.display = 'none';
                }, 3000);
            }).catch(err=>{
                console.log("Error: ", err)
            })
    }
    });
});
