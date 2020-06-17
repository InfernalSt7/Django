function comprobar(){
    confirm('¡Aquí tiene los últimos resultados!');
    setTimeout('comprobar()', 50000);    
}
comprobar()