$(function() {

	//regional es
	$.datepicker.regional['es'] = {
			 closeText: 'Cerrar',
			 prevText: '<Ant',
			 nextText: 'Sig>',
			 currentText: 'Hoy',
			 monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
			 monthNamesShort: ['Ene','Feb','Mar','Abr', 'May','Jun','Jul','Ago','Sep', 'Oct','Nov','Dic'],
			 dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
			 dayNamesShort: ['Dom','Lun','Mar','Mié','Juv','Vie','Sáb'],
			 dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','Sá'],
			 weekHeader: 'Sm',
			 dateFormat: 'dd/mm/yy',
			 firstDay: 1,
			 isRTL: false,
			 showMonthAfterYear: false,
			 yearSuffix: ''
			 };
	
	//Se seta como default el idioma español
	$.datepicker.setDefaults($.datepicker.regional['es']);
	
	// Date picker
	$("[id^='datepicker']").datepicker(
			{
				regional: "es",
				changeYear : true,
				showButtonPanel : true,
				dateFormat : 'dd/mm/yy',
					
				
				
				
				

				beforeShow : function(e, t) {
					$("#ui-datepicker-div").removeClass("hide-calendar");
					$("#ui-datepicker-div").removeClass('YearDatePicker');
					$("#ui-datepicker-div").removeClass('HideTodayButton');
				}, 
			});


	// Año Picker
	$("#aniopicker").datepicker(
			{
				changeYear : true,
				showButtonPanel : true,
				dateFormat : 'yy',
				regional: "es",


				beforeShow : function(e, t) {
					$(this).datepicker("hide");
					$("#ui-datepicker-div").addClass("hide-calendar");
					$("#ui-datepicker-div").addClass('YearDatePicker');
					$("#ui-datepicker-div").addClass('HideTodayButton');
				},

				onClose : function(dateText, inst) {
					var year = $(
							"#ui-datepicker-div .ui-datepicker-year :selected")
							.val();
					$(this).datepicker('setDate', new Date(year, 1));
				}
			});

	//Pop up para el alta de pases
	$("#pase_popup").dialog({
		autoOpen : false,
		height : 600,
		width : 800
	});

	//Evento para abrir el pop up de pases
	$("#popup").click(function() {

		$("#pase_popup").dialog("open");
	});

	//Evento para cerror el pop up de pases
	$("#close_popup").click(function() {

		$("#pase_popup").dialog("close");
	});

	// Cargar selección de combo en hidden input en cualquier select
	$("select[id^='select']").select().change(function() {

		var origen = $(this).attr('id').substring(6);

		var objetivo = "#input" + origen;

		$((objetivo)).val($(this).val());
	});

	// Validaciones para expediente
	$("#form-expediente-button").click(function(event) {

		var error = false;

		var div = document.getElementById('validate-div');
		var inputs = div.getElementsByTagName("input");

		$(inputs).each(function() {

			var origen = $(this).attr('id');

			if( origen != 'inputconsolidacion' & origen != 'checkconsolidacion'){
			
				var objetivo = "#" + origen + "-error";
	
				if ($(this).val() == "") {
					error = true;
					$(objetivo).removeClass('error_hide');
					$(objetivo).addClass('error_show');
				} else {
					$(objetivo).removeClass('error_show');
					$(objetivo).addClass('error_hide');
				}
			}
		});

		if (!error) {
			$("#form-expediente").submit();
		}

	});

	// Cargar selección del checkbox de consolidación
	$("[id^='check']").change(function() {

		var origen = $(this).attr('id').substring(5);
		var objetivo = "#input" + origen;
		$((objetivo)).val('');
		if($("[id^='check']").is(':checked')){		
			$((objetivo)).val('TRUE');
		}
		
	});


});
