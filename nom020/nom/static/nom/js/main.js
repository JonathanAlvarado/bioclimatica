$( document ).ready(function() {
	$('.six a').nivoLightbox({ effect: 'fade' });
	load_tables();

	get_states();

	$( "#estados" ).on('change', function() {
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

function load_tables(){
	$('.footable').footable();
}