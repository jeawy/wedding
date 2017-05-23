/*
 * common jquery functions
 *
 */

(function($){
    function getWidth() {
        if (self.innerWidth) {
            return self.innerWidth;
        }
        
        if (document.documentElement && document.documentElement.clientHeight) {
            return document.documentElement.clientWidth;
        }
        
        if (document.body) {
            return document.body.clientWidth;
        }
    }
    
    function getHeight() {
        if (self.innerHeight) {
            return self.innerHeight;
        }
        
        if (document.documentElement && document.documentElement.clientHeight) {
            return document.documentElement.clientHeight;
        }
        
        if (document.body) {
            return document.body.clientHeight;
        }
    }
     $.fn.extend({ 
                setBackgroundImg: function(urlPath) { 
                    var obj = $(this); 
                    urlPath = $.trim(urlPath || this.text());
                    if (!urlPath) {
                        return;
                    }
                     
                    obj.css("position", "fixed");
                    obj.css("top", "0"); 
                    obj.css("z-index", "-1000");
                    obj.css("background-repeat", "no-repeat");
                    obj.css("background-size", "100% 100%"); 
                 
                    
                    obj.css("height", getHeight());
                    obj.css("width", getWidth()); 
                    obj.css("background-image", urlPath); 
            }
     });
	
    
    
	
})(jQuery);
