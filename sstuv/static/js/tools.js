$(function() {

	
	
	/*
	 * Se setea el regional en el timepicker
	 */
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
	
	/*
	 * Se seta como default el idioma español
	 */
	$.datepicker.setDefaults($.datepicker.regional['es']);
	
	/* 
	 * Date picker
	 * 
	 */
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
	
	/* 
	 * Date picker
	 * 
	 */
	$("[id^='datepicker1']").datepicker(
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


	/*
	 *  Año Picker
	 */
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

	/*
	 * Popup que muestra mensaje de éxito al dar de alta un expediente.  
	 */
	$("#alta_expediente_success").dialog({
		autoOpen : false,
		height : 200,
		width : 300
	});
	
	/*
	 * SEteo del dialog para el pop up para el alta de pases
	 */
	$("#pase_popup").dialog({
		autoOpen : false,
		height : 600,
		width : 800
	});

	/*
	 * Evento para abrir el pop up de pases
	 * 
	 */
	$("#popup").click(function() {

		//Setea la fecha ene l pase
		$('#datepic').datepicker().datepicker('setDate', new Date());
		
		//
		$(('#panelExterno')).hide();

		
		//Abre el pop up
		$("#pase_popup").dialog("open");		
	});

	/*
	 * Evento para cerror el pop up de pases
	 */
	$("#close_popup").click(function() {

		$("#pase_popup").dialog("close");
	});

	/*
	 * Cargar selección de combo en hidden input en cualquier select
	 */ 
	$("select[id^='select']").select().change(function() {

		var origen = $(this).attr('id').substring(6);

		var objetivo = "#input" + origen;

		$((objetivo)).val($(this).val());
	});

	/*
	 *  Validaciones para expediente
	 */
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

			//popup de éxito
			$("#alta_expediente_success").dialog("open");
			
		}

	});
	
	/* 
	 *   Validaciones para salir de expediente
	 */ 
	$("#form-expediente-button-exit").click(function(event) {
		
		$("#continueInId").attr("value", "expedienteList");
		
		var div = document.getElementById('validate-div');
		var inputs = div.getElementsByTagName("input");

		var totalInputs = 0;
		var totalInputsVacio = 0; 
		
		$(inputs).each(function() {

			var origen = $(this).attr('id');

			if( origen != 'inputconsolidacion' & origen != 'checkconsolidacion'){
				totalInputs = totalInputs + 1;	
				if ($(this).val() == "") {
					totalInputsVacio = totalInputsVacio + 1;
				} 
			}
		});
		
		if (totalInputs == totalInputsVacio){
			$("#form-expediente").submit();
		}else{
			
			var error = false;
	
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
				$("#saveId").attr("value", "saveExpediente");
				$("#form-expediente").submit();
							
			}
		}

	});

	/*
	 * Cargar selección del checkbox de consolidación
	 */ 
	$("[id^='check']").change(function() {

		var origen = $(this).attr('id').substring(5);
		var objetivo = "#input" + origen;
		$((objetivo)).val('');
		if($("[id^='check']").is(':checked')){		
			$((objetivo)).val('TRUE');
		}
		
	});

	
	/*
	 * Muestra el chequ box de para departamentos externos
	 */ 
	$('#cheDep').click(function() {

		$(('#panelInterno')).show();
		$(('#panelExterno')).hide();
	});
	
	/*
	 * Muestra el chequ box de para departamentos internos
	 */ 
	$('#cheDep1').click(function() {

			$(('#panelExterno')).show();
			$(('#panelInterno')).hide();
	});
	
	
	
	/*
	 * 	Pop up para busqueda de expedientes
	 * 
	 */
	
	/*
	 * Seteo del dialogo
	 */
	$("#expediente_popup").dialog({
		autoOpen : false,
		height : 600,
		width : 800
	});

	/*
	 * Accion para abrir el dialogo
	 * 
	 */
	$("#expediente_popup_button").click(function() {
		$("#expediente_popup").dialog("open");		
	});
	
	/*
	 * 
	 *  Fin pop up para busqueda de expediente
	 */
	
	
	
	
	
	
	
});

