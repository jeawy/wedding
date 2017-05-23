
$(document).ready(function() {
    var $kb_container = $('.main_link_container');
    
    //read count
    $(document).on('touchstart click', ".fa-chevron-read", function() {
        
        var current = $(this);
        if($(this).hasClass("fa-chevron-down"))
        {
            $kb_container.find('.main_link_container_a').sort(function(a, b) { 
                var a_value = $(a).find('.fa-newspaper-o').text().replace ( /[^\d.]/g, '' );
                var b_value = $(b).find('.fa-newspaper-o').text().replace ( /[^\d.]/g, '' );
                var tmp =    b_value - a_value;
                return tmp;
            })
            .appendTo($kb_container);
            current.removeClass('fa-chevron-down');
            current.addClass('fa-chevron-up');
        }
        else{
            $kb_container.find('.main_link_container_a').sort(function(a, b) { 
            var a_value = $(a).find('.fa-newspaper-o').text().replace ( /[^\d.]/g, '' );
            var b_value = $(b).find('.fa-newspaper-o').text().replace ( /[^\d.]/g, '' );
            var tmp =  a_value - b_value  ;
            return tmp;
            })
            .appendTo($kb_container);
            current.removeClass('fa-chevron-up');
            current.addClass('fa-chevron-down');
        }
    });
    
    //date sort
     $(document).on('touchstart click', ".fa-chevron-date", function() {
        
        var current = $(this);
        if($(this).hasClass("fa-chevron-down"))
        {
            $kb_container.find('.main_link_container_a').sort(function(a, b) { 
                var a_value = $(a).find('.kbdate').text().replace ( /[^\d.]/g, '' );
                var b_value = $(b).find('.kbdate').text().replace ( /[^\d.]/g, '' );
                var tmp =    b_value - a_value;
                return tmp;
            })
            .appendTo($kb_container);
            current.removeClass('fa-chevron-down');
            current.addClass('fa-chevron-up');
        }
        else{
            $kb_container.find('.main_link_container_a').sort(function(a, b) { 
            var a_value = $(a).find('.kbdate').text().replace ( /[^\d.]/g, '' );
            var b_value = $(b).find('.kbdate').text().replace ( /[^\d.]/g, '' );
            var tmp =  a_value - b_value  ;
            return tmp;
            })
            .appendTo($kb_container);
            current.removeClass('fa-chevron-up');
            current.addClass('fa-chevron-down');
        }
    });
    //like sort
     $(document).on('touchstart click', ".fa-chevron-like", function() {
        
        var current = $(this);
        if($(this).hasClass("fa-chevron-down"))
        {
            $kb_container.find('.main_link_container_a').sort(function(a, b) { 
                var a_value = $(a).find('.fa-thumbs-up').text().replace ( /[^\d.]/g, '' );
                var b_value = $(b).find('.fa-thumbs-up').text().replace ( /[^\d.]/g, '' );
                var tmp =    b_value - a_value;
                return tmp;
            })
            .appendTo($kb_container);
            current.removeClass('fa-chevron-down');
            current.addClass('fa-chevron-up');
        }
        else{
            $kb_container.find('.main_link_container_a').sort(function(a, b) { 
            var a_value = $(a).find('.fa-thumbs-up').text().replace ( /[^\d.]/g, '' );
            var b_value = $(b).find('.fa-thumbs-up').text().replace ( /[^\d.]/g, '' );
            var tmp =  a_value - b_value  ;
            return tmp;
            })
            .appendTo($kb_container);
            current.removeClass('fa-chevron-up');
            current.addClass('fa-chevron-down');
        }
    });
    //comment count sort
     $(document).on('touchstart click', ".fa-chevron-comments", function() {
        
        var current = $(this);
        if($(this).hasClass("fa-chevron-down"))
        {
            $kb_container.find('.main_link_container_a').sort(function(a, b) { 
                var a_value = $(a).find('.fa-comment-o').text().replace ( /[^\d.]/g, '' );
                var b_value = $(b).find('.fa-comment-o').text().replace ( /[^\d.]/g, '' );
                var tmp =    b_value - a_value;
                return tmp;
            })
            .appendTo($kb_container);
            current.removeClass('fa-chevron-down');
            current.addClass('fa-chevron-up');
        }
        else{
            $kb_container.find('.main_link_container_a').sort(function(a, b) { 
            var a_value = $(a).find('.fa-comment-o').text().replace ( /[^\d.]/g, '' );
            var b_value = $(b).find('.fa-comment-o').text().replace ( /[^\d.]/g, '' );
            var tmp =  a_value - b_value  ;
            return tmp;
            })
            .appendTo($kb_container);
            current.removeClass('fa-chevron-up');
            current.addClass('fa-chevron-down');
        }
    });
    
     
});