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
        preview.className
        
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

        name.addEventListener("click", (e)=>{
            let data_inp = prompt("Enter to update value");
            updateData(item_datas[data].id, {name: data_inp});
        })
        detail.addEventListener("click", (e)=>{
            let data_inp = prompt("Enter to update value");
            updateData(item_datas[data].id, {detail: data_inp});
        })
        
    }   
}

// Update form control

let updateData = (id, datas)=>{
    fetch("/manage/admin/update/" + id, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(datas)
    }).then(response=>response.json())
    .then(data=>{
        console.log(data);
    }).catch(err=>{
        console.log(err);
    })
}