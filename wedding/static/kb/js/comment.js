$(document).ready(function() {
   
    
    /*************************************************************************
     * Comment Section
     */
   /*
  $(document).on('touchstart', "#comment_conent_btn", function() {
    event.preventDefault();  
    var current = $(this);
 
    var day_words_id =$('.word_id').val();
    var count =current.context.outerText;
    count = parseInt(count);
    var content = $("#day_words_comment_conent").val();
    
    $.post('/base/add_comment/', { day_words_id: day_words_id, content:content }, function(data) {
            var status = data['status'];
            var msg = data['msg'];
            $().message(msg); 
            if (status == '1')
            {
                var delay = 2000; //delay in milliseconds
                setTimeout(function() { location.reload(); }, delay);
            }  
        });
    });
    
    
    $(document).on('click', "#comment_conent_btn", function() {
    event.preventDefault();
    
    event.preventDefault();  
    var current = $(this);
 
    
    var day_words_id =$('.word_id').val();
    var count =current.context.outerText;
    count = parseInt(count);
    var content = $("#day_words_comment_conent").val();
    //var current = $(this);
     $.post('/base/add_comment/', { day_words_id: day_words_id, content:content }, function(data) {
            var status = data['status'];
            var msg = data['msg']; 
            $().message(msg); 
            if (status == '1')
            {
                var delay = 2000; //delay in milliseconds
                setTimeout(function() { location.reload(); }, delay);
            }  
        });
    });
    


*/
});
 function auto_grow(element) {
    element.style.height = "22px";
    element.style.height = (element.scrollHeight)+"px";
}
