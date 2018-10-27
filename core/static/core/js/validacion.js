

$(document).ready(function() {
    $("#formularioFundacion").validate({
        rules:{
            txtRut: {
                required:true,
                minlength:3,
                maxlength:30

            },
            txtNombreCompleto: {
                required:true,
                minlength:5,
                maxlength:60,
                number :false
                
            },
            dtpFechaNacimiento: {
                required:true,
                date:true,
                minlength:8
               
            },
            txtEmail: {
                required:true,
                minlength:3,
                maxlength:30,
                email:true
            },
            txtTelefono: {
                required:true,
                minlength:3,
                maxlength:30,
                number :true
                
            },
            cboRegion: {
                required:true
            },
            cboCiudad:{
                required:true
            },
            cboVivienda:{
                required:true
            },
        },
        messages:{
            txtRut:{
                required:"Ingrese un Rut valido"
            },
            txtNombreCompleto:{
                required:"Ingrese solo caracteres"
                //email:true
                //date:true
            },
            txtTelefono:{
                required:"Ingrese Numero telefonico",
                text:false
            },
            dtpFechaNacimiento:{
                required:"Ingrese una fecha valida",
                date:true,
            },
            txtEmail:{
                required:"Ingrese con formato de correo valido",
                email:true,
            },
            cboRegion:{
                required:"Seleccione una Region"
            },
            cboCiudad:{
                required:"Seleccione una Ciudad"
            },
            cboVivienda:{
                required:"Seleccione tipo de Vivienda"
            },
        }
    });
});