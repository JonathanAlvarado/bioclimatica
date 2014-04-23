$( document ).ready(function() {
	load_tables();
	
	$( "#id_state" ).on('change', function() {
		get_cities( $(this).val() );
	});

	$( "#id_house_part" ).on('change', function() {
		get_ubication( $(this).val() );
	});

});

function load_tables(){
	$('.footable').footable();
}

function get_cities( edo ){
	Dajaxice.nom.update_city( Dajax.process, { 'option':edo } )
}

function get_ubication( hpart ){
	Dajaxice.nom.get_ubication( Dajax.process, { 'hpart':hpart } )
	Dajaxice.nom.get_materials( Dajax.process, { 'house_part':hpart } )
}

function submit_material(){
	h_part = $('#id_house_part').val();
	ubication = $('#id_ubication').val();
	material = $('#id_material').val();
	area = $('#id_area').val();
	Dajaxice.nom.submit_material( Dajax.process, { 'h_part':h_part, 'ubication':ubication, 'material':material, 'area':area } )
}

function ajax_table(data){
	$('table tbody').append(data).trigger('footable_redraw');
}

function send_form(){
	Dajaxice.nom.calculate( Dajax.process, { 'city':$('#id_city').val(), 'floors':$('#id_nfloor').val() } );
}

function result(data){
	alert(data)
}