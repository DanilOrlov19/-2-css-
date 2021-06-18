
$(document).ready(function(){

$('#div_id_buying_type').val('self Самовывоз осуществляется по адресу ул.Ленина,101');
  $('select').on('change', function(e) {
    	$('#price').text($(this).val());
});
});