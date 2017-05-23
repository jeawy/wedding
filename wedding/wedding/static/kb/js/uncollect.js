$(document).ready(function() {
    var love='喜欢';
  $(document).on('touchstart', ".fa-thumbs-up", function() {
    event.preventDefault(); 
    var current = $(this);
    
    
    var kbid = $('#kbid').val();
    var count =current.context.outerText;
    //get ingeter from string
    count = count.match(/\d/g).join("");
    count = parseInt(count);
     if (count <= 0)
        return;
    
    $.post('/good/del/', { kbid: kbid }, function(data) {
        var status = data['status'];
        var msg = data['msg'];
        
        if (status == '1')
        {
             $().message(msg); 
            var delay = 3000; //delay in milliseconds
            setTimeout(function() { $(window.location).attr('href', '/login/?next='+window.location.pathname); }, delay);
        }
        else{
             if (status == '0')
            {
                current.removeClass('fa-thumbs-up');
                current.addClass('fa-thumbs-o-up'); 
                current.text(love + (count-1).toString());
                //current.text(count-1);
            }
            else
            {
                $().message(msg); 
            }
        }
            
        });
    });
    
$(document).on('click', ".fa-heart", function() {
    event.preventDefault();
    var current = $(this);  
    var kbid = $('#kbid').val(); 
    
    $.post('/kb/collect_del_kb/', { kbid: kbid }, function(data) {
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
                    current.removeClass('fa-heart');
                    current.addClass('fa-heart-o'); 
                    current.text('收藏');
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