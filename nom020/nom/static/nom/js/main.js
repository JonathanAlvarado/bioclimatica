$( document ).ready(function() {

	$( "#id_estado" ).on('change', function() {
  		display_cities( $(this).val() );
  	});
  
})

function display_cities(edo){
	Dajaxice.nom.update_city( Dajax.process, {'option':edo} );
}

function send_form(){
    Dajaxice.nom.send_form(Dajax.process,{'form':$('#data_form').serialize(true)});
}

function my_js_callback(data){
	alert(data.message);
}

function calculate(){
	Dajaxice.nom.multiply(Dajax.process,{'a':$('#a').val(),'b':$('#b').val()})
}