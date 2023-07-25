let orders = []
let message = document.querySelector(".message");
window.onload =
    fetch("/orders/items").then(response=>response.json())
                    .then(datas=>{
                        if(datas){
                            for(data in datas){
                                orders.push({
                                    order_id: datas[data][0],
                                    count: datas[data][2],
                                    product_name: datas[data][1]
                                })
                            }
                            console.log(orders)
                            show_orders();
                        }  
                    }).catch(err=>{
                        console.log('Error: ', err);
                    })                   


let show_orders = ()=>{
    for(order in orders){
        let orders_ = document.createElement("div");
        orders_.className = "orders";
        document.querySelector(".user_orders").appendChild(orders_);
        let product_name = document.createElement("div");
        product_name.className = "product_name";
        product_name.innerText = orders[order].product_name;
        orders_.appendChild(product_name);
        let count = document.createElement("div");
        count.className = "count";
        count.innerText = orders[order].count;
        orders_.appendChild(count);
        let option = document.createElement("div");
        option.className = "option";
        orders_.appendChild(option);
        let cancal = document.createElement("div");
        cancal.className = "cancal";
        cancal.innerText = "Cancal";
        cancal.content = order;
        option.appendChild(cancal);
        let confirm = document.createElement("div");
        confirm.className = "confirm";
        confirm.innerText = "Confirm";
        confirm.content = order;
        option.appendChild(confirm);
        
        confirm.addEventListener("click", (e)=>{
            let confirm_item = orders[e.target.content]
            order_confirm(confirm_item.order_id);
        });

        cancal.addEventListener("click", (e)=>{
            let data = {
                order_id: orders[e.target.content].order_id
            }
            fetch("/orders/order_cancal",{
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(response=>response.json())
            .then(datas=>{
                if(datas){
                    message.style.backgroundColor = "brown";
                    message.style.display = 'block';
                    message.style.color = "whitesmoke";
                    message.innerText = datas.message;
                    setTimeout(()=>{
                        message.style.display = 'none';
                        window.location.href = "/orders";
                    }, 2000);
                }
            }).catch(err=>{
                console.log('Error: ', err);
            })
        })
    }
}

let order_confirm = (order_id)=>{
    const URL = "/orders/order_confirm";
    let datas = {
        order_id: order_id
    }
    fetch(URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(datas)
    }).then(response=>response.json())
              .then(datas=>{
                if(datas){
                    message.style.display = 'block';
                    message.innerText = datas.message;
                    setTimeout(()=>{
                        message.style.display = 'none';
                        window.location.href = "/orders";
                    }, 2000);
                }
              }).catch(err=>{
                console.log("Error: ", err);
              })
}