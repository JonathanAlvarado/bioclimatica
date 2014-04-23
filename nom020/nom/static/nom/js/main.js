$( document ).ready(function() {
	alert('si');
	load_tables();

	$( "#id_state" ).on('change', function() {
		display_cities( $(this).val() );
	});

	/*$( "#house_part" ).on('change', function() {
		get_materials();
	});*/

});

function display_cities(edo){
	alert(edo);
	//Dajaxice.nom.update_city( Dajax.process, {'option':edo} )
}

/*function send_form(){
    Dajaxice.nom.send_form(Dajax.process,{'form':$('#data_form').serialize(true)});
}*/

function calculate(){
	Dajaxice.nom.multiply(Dajax.process,{'a':$('#a').val(),'b':$('#b').val()})
}

function get_materials(){
	//alert( $('#house_part').val() );
	//Dajaxice.nom.get_materials( Dajax.process, {'house_part:':$('#house_part').val()} )
}

function load_tables(){
	$('.footable').footable();
}

function submit_material(){
	h_part = $('#house_part').val();
	ubication = $('#ubication').val();
	material = $('#material').val();
	area = $('#area').val();
	Dajaxice.nom.submit_material( Dajax.process,{ 'h_part':h_part, 'ubication':ubication, 'material':material, 'area'area } )
}