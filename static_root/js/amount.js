$(function(){
	$('.quantity').keyup(function(){
		
		$x = ($(this).next()).attr('id')
			$.ajax({
            type: "POST",
            url: "/local/amtfind/",
            data: {
                'search_data' :  $(this).val(),
				'dist' : $('#dist').val(),
				'rate' : $(this).prev().val(),
			
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data){
				

				$x = '#' + $x ;
				
                
                $($x).val(data)
                $amount = 0;
                
                $('.amt').each(function(){


                        $amount = parseFloat($amount) + parseFloat(($(this).val()));
                            });
                
                $('#total').val($amount)
				
			},
            dataType: 'html'
			
			
			
        });
		
		
	});
});
