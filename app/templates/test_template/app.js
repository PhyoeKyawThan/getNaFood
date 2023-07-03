let items_tag = {
    image: document.querySelectorAll("#item-src"),
    name: document.querySelectorAll("#item-name"),
    description: document.querySelectorAll("#description")
};
let items = {
    item_name: "PhyoeKyawThan",
    item_src: "./product.jpg",
    description: "The best product for play with feeling and can leave alone when u getting bored."
};

window.onload = (e)=>{
    items_tag.image.forEach(img => {
        img.src = items.item_src;
    });
    items_tag.name.forEach(name =>{
        name.textContent = items.item_name;
    });
    items_tag.description.forEach(des =>{
        des.textContent = items.description;
    });
};