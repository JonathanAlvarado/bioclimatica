var postUrl = "http://localhost:8000/nom/";

$( document ).ready(function() {

	$( "#id_estado" ).on('change', function() {
  		display_cities( $(this).val() );
  	});
  
})

function display_cities(edo){
    alert(edo);
	
}