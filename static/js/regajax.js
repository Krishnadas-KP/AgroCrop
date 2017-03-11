
$(function(){
	
	$(".district").change(function(){
			$x = (($(this).next()).attr('id'))
		$.ajax({
            type: "POST",
			
            url: "/home/rlogic/",
		
            data: {
                'search_text' : $(this).val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val(),

            },
			
            success: function(data){
				
				
				$x = '#' + $x ;
				
                $($x).html(data)
				
			},
            dataType: 'html'
        });
	});

});
