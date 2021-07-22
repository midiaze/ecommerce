let id_producto_eliminar = -1;

function establecer_eliminar_producto_id(id) {
    id_producto_eliminar = id;
}

function eliminar_producto() {
    window.location.href = "/productos/eliminar_producto/" + id_producto_eliminar;
}




// const productos = [
//     {nombre: 'Platanos', Valor: 500},
//     {nombre: 'Pera', Valor: 500},
//     {nombre: 'Sandia', Valor: 500},
//     {nombre: 'Melon', Valor: 500},
//     {nombre: 'Frutillas', Valor: 500},
// ]


// const formulario = document.querySelector('#formulario');
// const boton = document.querySelector('#boton');
// const resultado = document.querySelector('#resultado');

// const filtrar = ()=>{

//     resultado.innerHTML = '';

//     const texto = formulario.value.toLowerCase();

//     for(let producto of productos){
//         let nombre = producto.nombre.toLowerCase();
//         if(nombre.indexOf(texto) !== -1){
//             resultado.innerHTML += `
//             <li>${producto.nombre} - Valor: ${producto.Valor}</li>
//             `

//         }
//     }

//     if(resultado.innerHTML === ''){
//         resultado.innerHTML += `
//             <li>Producto no encontrado...</li>
//             `
//     }
// }

// boton.addEventListener('click', filtrar)
// formulario.addEventListener('keyup', filtrar)

// filtrar();
