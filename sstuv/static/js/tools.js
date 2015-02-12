
$(function() {
	
	//
	$(document).ready(function() {

		$.datepicker.setDefaults($.datepicker.regional['es']);

		$("input[id^='datepicker']").datepicker();

	});

	//
	$("#pase_popup").dialog({
		autoOpen : false,
		height : 600,
		width : 800
	});

	//
	$("#popup").click(function() {

		$("#pase_popup").dialog("open");
	});

	//
	$("#close_popup").click(function() {

		$("#pase_popup").dialog("close");
	});

	//Cargar selección de combo en hidden input
	$("select[id^='select']").select().change(function() {

		var origen = $(this).attr('id').substring(6);

		var objetivo = "#input" + origen;

		$((objetivo)).val($(this).val());
	});

	// Validaciones para expediente
	$("#form-expediente-button").click(function(event){
		
		var error=false;
		
		var div = document.getElementById('validate-div');
		var inputs = div.getElementsByTagName("input");	
		
		
		$(inputs).each(function() {
        	
        	var origen = $(this).attr('id');

    		var objetivo = "#" + origen + "-error";
   	
        	if($(this).val() == ""){ 
    			error=true;
    			$(objetivo).removeClass('error_hide');
    			$(objetivo).addClass('error_show');
    		}else{
    			$(objetivo).removeClass('error_show');
    			$(objetivo).addClass('error_hide');
    		}
        });
	
        if(!error){
			$("#form-expediente").submit();
		}
		
	});
	
	
	


});
