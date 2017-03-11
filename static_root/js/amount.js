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
				
				
                $($x).html(data)
				
				
			},
            dataType: 'html'
			
			
			
        });
		
		
	});
});

