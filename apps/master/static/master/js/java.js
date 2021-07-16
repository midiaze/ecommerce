cargarDatos();

function agregarAlCarrito(modelo, id){
    let cantidad = document.getElementById(id);
    modelo['cantidad'] = cantidad.value
    let item = JSON.stringify(modelo);
    localStorage.setItem(id, item);
    cargarDatos();
}

function cargarDatos(){
    let contenido = document.getElementById('contenido');
    for(let i=0; i=localStorage.length; i++){
        let item= localStorage.getItem(localStorage.key[i]);
        let json = JSON.parse(item);

        let div = document.createElement('div');
        div.classList.add('producto');

        let h4 = document.createElement('h4');
        h4.innerHTML = json.nombre;
        div.appendChild(h4);

        let img = document.createElement('img');
        img.src = 'static/master/img/carrito.png'
        div.appendChild(img);
        contenido.appendChild(div);
    }
}
