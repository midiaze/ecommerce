let id_usuario_inactivar = -1;

function establecer_eliminar_id(id) {
    id_usuario_inactivar = id;
}

function eliminar() {
    window.location.href = "/usuarios/inactivar_usuario/" + id_usuario_inactivar;
}