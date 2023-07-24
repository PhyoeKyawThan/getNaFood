let item_datas = []
window.onload = fetch("/request/get_item_datas").then(response=>response.json())
.then((datas)=>{
    for(id in datas){
        item_datas.push({
            id : datas[id][0],
            product_name: datas[id][1],
            detail: datas[id][2],
            price: datas[id][3],
            count: datas[id][4],
            img_path: datas[id][5]
        });
    }
    showData(item_datas);
}).catch((err)=>{
    console.log(err);
})

// data insert
let datas_name = ["id", "name", "detail", "price", "count"]
let table = document.querySelector(".table");
let showData = (datas)=>{
    for(data in datas){
        let items = document.createElement("div");
        items.className = "items";
        table.appendChild(items);
        let id = document.createElement("div");
        let name = document.createElement("div");
        let detail = document.createElement("div");
        let price = document.createElement("div");
        let count = document.createElement("div");
        let preview = document.createElement("div");
        let img = document.createElement("img");
        // unique id
        id.content = data;
        name.content = data;
        detail.content = data;
        price.content = data;
        count.content = data;
        img.content = data;
        // edit section 
        let edit = document.createElement("div");
        edit.className = "edit";
        let delete_ = document.createElement("div");
        delete_.className = "delete";
        let delete_link = document.createElement("a");
        delete_link.innerText = "DELETE";
        delete_link.style.color = 'white';
        delete_.appendChild(delete_link).href = "/manage/admin/delete/"+datas[data].product_name;

        items.appendChild(id).innerText = Number(data)+1;
        items.appendChild(name).innerText = datas[data].product_name;
        items.appendChild(detail).innerText = datas[data].detail;
        items.appendChild(price).innerText = datas[data].price;
        items.appendChild(count).innerText = datas[data].count;
        items.appendChild(preview);
        preview.appendChild(img).src = "/static/"+datas[data].img_path;
        items.appendChild(edit);
        edit.appendChild(delete_);

        // update items
        name.addEventListener("click", (e)=>{
            let data_inp = prompt("Enter to update value");
            if(data_inp){
                name.innerText = updateData(item_datas[e.target.content].id, name, {product_name: data_inp});
            }
        });
        detail.addEventListener("click", (e)=>{
            let data_inp = prompt("Enter to update value");
            if(data_inp){
                updateData(item_datas[e.target.content].id, detail, {description: data_inp});
            }
        });
        price.addEventListener("click", (e)=>{
            let data_inp = prompt("Enter to update value");
            if(data_inp){
                updateData(item_datas[e.target.content].id, price, {price: data_inp});
            }
        });
        count.addEventListener("click", (e)=>{
            let data_inp = prompt("Enter to update value");
            if(data_inp){
                updateData(item_datas[e.target.content].id, count, {count: data_inp});
            }
        });
        preview.addEventListener("click", (e)=>{
            let id = e.target.content;
            let div = document.createElement("div");
            let form = document.createElement("form");
            div.appendChild(form);
            table.appendChild(div);
            div.style.textAlign = "center";
            form.setAttribute("enctype", "multipart/form-data");
            table.appendChild(form);
            let input = document.createElement("input");
            input.setAttribute("type", "file");
            input.name = "img";
            form.setAttribute("style", "position: fixed; top: 0; background-color: grey; text-align: center; width: 100%")
            form.appendChild(input);
            input.addEventListener("change", (e)=>{
                let uploadOrNot = confirm("Do u want to upload?");
                let formData  = new FormData();
                formData.append("img", e.target.files[0]);
                if(uploadOrNot){
                    fetch("http://127.0.0.1:5000/manage/admin/update/product_image/" + item_datas[id].id, {
                        method: "POST",
                        body: formData
                    }).then(response=>response.json())
                    .then(datas=>{
                         if(datas.status === 200 || datas.status === 403){
                            img.src = "/static/" + datas.updated_data;
                            form.style.display = "none";
                         }
                    }).catch(err=>{
                        console.log("Error: ", err);
                    })
                }
            })
            })
    }   
}

// Update form control

let updateData = (id, element, datas)=>{
    let change;
    fetch("/manage/admin/update/" + id, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(datas)
    }).then(response=>response.json())
    .then(datas=>{
        element.innerText = datas.updated_data;
    }).catch(err=>{
        console.log(err);
    })
}
