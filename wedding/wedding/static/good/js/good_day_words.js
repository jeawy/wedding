$(document).ready(function() {
    var love = '喜欢';
    $(document).on('touchstart', ".fa-heart-o", function() {
    event.preventDefault(); 
    var is_authenticated =$('#is_authenticated').val();
    var current = $(this);
    if (is_authenticated.toLowerCase() == 'false')
    {
            $().message('请先登录...'); 
            var delay = 3000; //delay in milliseconds
            setTimeout(function() { $(window.location).attr('href', '/login/'); }, delay);
            return;
    }
    
    var day_words_id =current.parent().find('.word_id').val()
    var count =current.context.outerText;
    //get ingeter from string
    count = count.match(/\d/g).join("");
    count = parseInt(count);
   
    //var current = $(this);
    $.post('/good/add/', { day_words_id: day_words_id }, function(data) {
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
                current.addClass('fa-heart');
                current.removeClass('fa-heart-o');
                current.text(love + (count+1).toString());
            }
            else
            {
                $().message(msg); 
            }
        }
            
        });
    });
    $(document).on('click', ".fa-heart-o", function() {
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
    //get ingeter from string
    count = count.match(/\d/g).join("");
    count = parseInt(count);
   
    //var current = $(this);
    $.post('/good/add/', { day_words_id: day_words_id }, function(data) {
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
                
                current.addClass('fa-heart');
                current.removeClass('fa-heart-o');
                //current.text(count+1);
                current.text(love + (count+1).toString());
            }
            else
            {
                $().message(msg); 
            }
        }
            
        });
    });
    
    
    
    
    /*************************************************************************
     * Comment Section
     */
    /*
  $(document).on('touchstart', ".fa-comment-o", function() {
    event.preventDefault(); 
    var is_authenticated =$('#is_authenticated').val();
    var current = $(this);
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
    //var current = $(this);
    $.post('/base/start_comment/', { day_words_id: day_words_id }, function(data) {
        var status = data['status'];
        var msg = data['msg'];
        
       
             if (status == '0')
            {
                current.text(count+1);
            }
            else
            {
                $().message(msg); 
            }
            
        });
    });
    $(document).on('click', ".fa-comment-o", function() {
    event.preventDefault();
    
    event.preventDefault(); 
    var is_authenticated =$('#is_authenticated').val();
    var current = $(this);
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
    var content = "test content";
    //var current = $(this);
    $.post('/base/start_comment/', { day_words_id: day_words_id, content : content }, function(data) {
        var status = data['status'];
        var msg = data['msg'];
        
       
             if (status == '0')
            {
                current.text(count+1);
            }
            else
            {
                $().message(msg); 
            }
            
        });
    });
    */
});