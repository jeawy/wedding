$(document).ready(function() {
  $(document).on('touchstart', ".fa-heart", function() {
    event.preventDefault(); 
    var current = $(this);
    
    var is_authenticated =$('#is_authenticated').val();
    if (is_authenticated.toLowerCase() == 'false')
    {
            $().message('请先登录...'); 
            var delay = 3000; //delay in milliseconds
            setTimeout(function() { $(window.location).attr('href', '/login/'); }, delay);
            return;
    }
    var day_words_id =current.parent().find('.word_id').val()
    var count =current.context.outerText;
    count = parseInt(count);
     if (count <= 0)
        return;
    
    $.post('/good/del/', { day_words_id: day_words_id }, function(data) {
        var status = data['status'];
        var msg = data['msg'];
        
        if (status == '1')
        {
             $().message(msg); 
            var delay = 3000; //delay in milliseconds
            setTimeout(function() { $(window.location).attr('href', '/login/'); }, delay);
        }
        else{
             if (status == '0')
            {
                current.removeClass('fa-heart');
                current.addClass('fa-heart-o'); 
                current.text(count-1);
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
    var is_authenticated =$('#is_authenticated').val();
    if (is_authenticated.toLowerCase() == 'false')
    {
         $().message('请先登录...'); 
            var delay = 3000; //delay in milliseconds
            setTimeout(function() { $(window.location).attr('href', '/login/'); }, delay);
            return;
    }
    
    var day_words_id = current.parent().find('.word_id').val()
    var count = current.context.outerText;
    count = parseInt(count);
     if (count <= 0)
        return;
    
    $.post('/good/del/', { day_words_id: day_words_id }, function(data) {
        var status = data['status'];
        var msg = data['msg'];
        
        if (status == '1')
        {
            $().message(msg); 
            var delay = 3000; //delay in milliseconds
            setTimeout(function() { $(window.location).attr('href', '/login/'); }, delay);
        }
        else{
             if (status == '0')
            {
                current.removeClass('fa-heart');
                current.addClass('fa-heart-o'); 
                current.text(count-1);
            }
            else
            {
                $().message(msg); 
            }
        }
            
        });
    });
});