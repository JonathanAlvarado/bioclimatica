$( document ).ready(function() {

	$( "#id_estado" ).on('change', function() {
  		display_cities( $(this).val() );
  	});
  
})

function display_cities(edo){
	Dajaxice.nom.update_city( Dajax.process, {'option':edo} );
}