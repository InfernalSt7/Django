function refrescar(){
    var cargando = confirm("Imprima esta página")
    if (cargando) {
        window.print()
    }
}
refrescar()