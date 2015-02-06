

$(function() {
	$(document).ready(function() {

		$.datepicker.setDefaults($.datepicker.regional['es']);

		$("input[id^='datepicker']").datepicker();

	});
	
   
	$( "#pase_popup" ).dialog({
	       autoOpen: false, 
	       height: 600,
	       width:800 
	    });
	    
	
	$( "#popup" ).click(function() {
	   	
	       $( "#pase_popup" ).dialog( "open" );
	    });
	    
	    
	$( "#close_popup" ).click(function() {
	       	
	        $( "#pase_popup" ).dialog( "close" );
	   });
	 
 
	$("select[id^='select']").select().change(function() {
		
		var origen=$(this).attr('id').substring(6)
		
		var objetivo = "#input" + origen;
	
		$((objetivo)).val ( $(this).val()); 
	});  
    
});

