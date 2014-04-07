$( document ).ready(function() {
	load_tables();

	get_states();

	$( "#states" ).on('change', function() {
  		display_cities( $(this).val() );
  	});

});

function get_states(){
	Dajaxice.nom.get_states( Dajax.process )
}

function display_cities(edo){
	Dajaxice.nom.update_city( Dajax.process, {'option':edo} )
}

/*function send_form(){
    Dajaxice.nom.send_form(Dajax.process,{'form':$('#data_form').serialize(true)});
}*/

function calculate(){
	Dajaxice.nom.multiply(Dajax.process,{'a':$('#a').val(),'b':$('#b').val()})
}

function get_materials(){
	Dajaxice.nom.get_materials( Dajax.process )
}

function load_tables(){
	$('.footable').footable();
}

function ajax_table(data){

}

function submit_material(){
	h_part = $('#house_part').val();
	ubication = $('#ubication').val();
	material = $('#material').val();
	area = $('#area').val();
	Dajaxice.nom.submit_material( Dajax.process,{ 'h_part':h_part, 'ubication':ubication, 'material':material, 'area'area } )
}