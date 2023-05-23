const BASE_URL = "http://localhost:8000";

function redireccionar(url,id) {
    window.location.href=url+"/"+id;
}

function volver(url) {
    document.location.href=BASE_URL+url
}

function agregar_carrito(id_inv) {
    let campo_inv = document.getElementById('id_inv');
    campo_inv.value=id_inv;
}