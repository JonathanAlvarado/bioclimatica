$( document ).ready(function() {
	load_tables();

	get_states();

	$( "#states" ).on('change', function() {
  		display_cities( $(this).val() );
  	});

});

/*function calculate(){
	Dajaxice.nom.multiply(Dajax.process,{'a':$('#a').val(),'b':$('#b').val()})
}*/

function load_tables(){
	$('.footable').footable();
}

function get_states(){
	Dajaxice.nom.get_states( Dajax.process )
}

function display_cities(edo){
	Dajaxice.nom.update_city( Dajax.process, { 'option':edo } )
}

function get_ubication(){
	Dajaxice.nom.get_ubication( Dajax.process, { 'hpart':$('#house_part').val() } )
	Dajaxice.nom.get_materials( Dajax.process, { 'house_part':$('#house_part').val() } )
}

function submit_material(){
	h_part = $('#house_part').val();
	ubication = $('#ubication').val();
	material = $('#material').val();
	area = $('#area').val();
	Dajaxice.nom.submit_material( Dajax.process, { 'h_part':h_part, 'ubication':ubication, 'material':material, 'area':area } )
}

function ajax_table(data){
	$('table tbody').append(data).trigger('footable_redraw');
}

function send_form(){
    Dajaxice.nom.calculate( Dajax.process, { 'city':$('#cities').val(), 'floors':$('#floors').val() } );
}

function result(data){
	if ( data == "error" ) {
		$( ".error" ).show();
	}else{
		$( ".error" ).hide();
		$( "#result" ).html( "Eficiente en un "+ data );
	}
}

function validateForm() {
	var isValid = true;
	
	$('.form-field').each(function() {
		if ( $(this).val() === '0' ){
			$(this).css( { "border": '#FF0000 1px solid'} );
			isValid = false;
		}
	});

	if ( isValid ){
		send_form();
	}
}