$(document).ready(function() {

	// Add Style to dimension switch checkbox
	$('#dimension-switch').bootstrapSwitch();
	
	// Set CSS page layout if already selected
	if($.cookie != undefined){
		$('link[href*="custom/custom-bootstrap"]').attr('href',$.cookie('css-style'));
	}

	$('#simple').click(function (){
		$.cookie('css-style', 'custom/custom-bootstrap_simple.css', { expires: 7, path: '/' });
		$('link[href*="custom/custom-bootstrap"]').attr('href',$.cookie('css-style'));
		});
	$('#red').click(function (){
		$.cookie('css-style', 'custom/custom-bootstrap_red.css', { expires: 7, path: '/' });
		$('link[href*="custom/custom-bootstrap"]').attr('href',$.cookie('css-style'));
		});
	$('#blue').click(function (){
		$.cookie('css-style', 'custom/custom-bootstrap_blue.css', { expires: 7, path: '/' });
		$('link[href*="custom/custom-bootstrap"]').attr('href',$.cookie('css-style'));
		});
	
	// Change layout with checkbox
	$('#dimension-switch').change(function () {

		if($(this).prop('checked')) {
			$('link[href="custom/custom-bootstrap_simple.css"]').attr('href','custom/custom-bootstrap_red.css');
			$.cookie('css-style', 'custom/custom-bootstrap_red.css', { expires: 7, path: '/' });
			} else {

				$('link[href="custom/custom-bootstrap_red.css"]').attr('href','custom/custom-bootstrap_simple.css');
				$.cookie('css-style', 'custom/custom-bootstrap_simple.css', { expires: 7, path: '/' });
			}

			});


	});


