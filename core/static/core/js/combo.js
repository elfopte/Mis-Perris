$(document).ready(function() {

    var cboRegion  = $("#cboRegion");

    cboRegion.change(function() {
        var id_region = cboRegion.val();

        if(id_region=="") {
            $("#cboCiudad").prop("disabled", true);
            $("#cboCiudad").val("");
            return;
        }

        //enviamos una peticion a combo.php
        //enviandole el id de la region
        $.get("combo.php", {id_region:id_region}, function(respuesta) {
            
            //dejamos los option dentro del cboCiudad con la funcion .html
            $("#cboCiudad").html(respuesta);
            //habilitamos el combobox de ciudad
            $("#cboCiudad").prop("disabled", false);

        });

    });

});