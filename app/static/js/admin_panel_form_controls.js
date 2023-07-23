// form control

let add_new = document.getElementById("add");

add_new.addEventListener("click", (e)=>{
    e.preventDefault();
    let add_form = document.getElementById("add_new");
    if(add_form.style.display === 'block'){
        add_form.style.display = 'none';
    }else{
        add_form.style.display = 'block';
    }
})



let add = document.getElementById("button");

add.addEventListener("click", ()=>{
    let image = document.querySelector(".img");
    let name = document.getElementById("name");
    let detail = document.getElementById("detail");
    let price = document.getElementById("price");
    let count = document.getElementById("count");

    let form = new FormData();

    form.append("image", image.files[0]);
    let values = [name, detail, price, count]
    let data_names = ["name", "detail", "price", "count"];
    for(data in data_names){
        form.append(data_names[data], values[data].value)
    }
    
    const URL = '/add_product';
    fetch(URL, {
        method: 'POST',
        body: form
    }).then((response)=>response.json()
    ).then((datas)=>{
        console.log("Response: ", datas);
        window.location.href = datas.redirect;
    }).catch((err)=>{
        console.log(err);
    })
    
})


let file_inp = document.querySelector("#image");
let img = document.querySelector("#img");

file_inp.addEventListener("change", (e)=>{
    let file = e.target.files[0];
    let fileObj = new FileReader();

    fileObj.addEventListener("load", ()=>{
        img.setAttribute("src", fileObj.result);
    });
    fileObj.readAsDataURL(file);
});



