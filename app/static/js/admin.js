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

let add = document.getElementById("button");

// data send
//select tag
let img_file = document.getElementById("image");
let product_name = document.getElementById("name");
let description = document.getElementById("detail");
add.addEventListener("click", (e)=>{
    e.preventDefault();

    const formData = new FormData();
    formData.append('image', img_file.files[0]);
    formData.append('name', product_name.value);
    formData.append('detail', description.value);

    const URL = '/add_product'
    fetch('/add_product', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        console.log('Response:', data);
        // Handle response from the Flask application
      })
      .catch(error => {
        console.error('Error:', error);
        // Handle errors
      });
});