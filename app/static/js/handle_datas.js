let items = []
window.onload = fetch("/request/get_item_datas").then(response=>response.json())
.then((datas)=>{
    for(id in datas){
        items.push({
            id : datas[id][0],
            product_name: datas[id][1],
            detail: datas[id][2],
            price: datas[id][3],
            count: datas[id][4],
            img_path: datas[id][5]
        });
    }
    showData(items);
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
        
        // edit section 
        let edit = document.createElement("div");
        let delete_ = document.createElement("div");
        delete_.className = "delete";
        let update = document.createElement("div");
        update.className = "update";

        items.appendChild(id).innerText = datas[data].id;
        items.appendChild(name).innerText = datas[data].product_name;
        items.appendChild(detail).innerText = datas[data].detail;
        items.appendChild(price).innerText = datas[data].price;
        items.appendChild(count).innerText = datas[data].count;
        items.appendChild(preview);
        preview.appendChild(img).src = "/static/"+datas[data].img_path;
        
}   

}
