$(document).ready(function() {
     
    $(document).on('touchstart', ".fa-heart-o", function() {
    event.preventDefault();  
     var current = $(this); 
    var kbid = $('#kbid').val();
      
    $.post('/kb/collect_kb/', { kbid: kbid }, function(data) {
        var status = data['status'];
        var msg = data['msg'];
        
        if (status == '1')
        {
            $().errormessage(msg); 
            var delay = 3000; //delay in milliseconds
            setTimeout(function() { $(window.location).attr('href', '/login/?next='+window.location.pathname); }, delay);
        }
        else{
             if (status == 'OK')
            { 
                current.addClass('fa-heart');
                current.removeClass('fa-heart-o'); 
                current.text('已收藏');
                $().message(msg); 
            }
            else
            {
                $().errormessage(msg); 
            }
        }
            
        });
    });
    $(document).on('click', ".fa-heart-o", function() {
    event.preventDefault();
    
    var current = $(this); 
    var kbid = $('#kbid').val();
      
    $.post('/kb/collect_kb/', { kbid: kbid }, function(data) {
        var status = data['status'];
        var msg = data['msg'];
        
        if (status == '1')
        {
            $().errormessage(msg); 
            var delay = 3000; //delay in milliseconds
            setTimeout(function() { $(window.location).attr('href', '/login/?next='+window.location.pathname); }, delay);
        }
        else{
             if (status == 'OK')
            { 
                current.addClass('fa-heart');
                current.removeClass('fa-heart-o'); 
                current.text('已收藏');
                $().message(msg); 
            }
            else
            {
                $().errormessage(msg); 
            }
        }
            
        });
    }); 
});