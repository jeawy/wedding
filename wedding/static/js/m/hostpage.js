 
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
    
    
     $(function() {
        //var screenwidth = window.innerWidth;
        var screenwidth = document.body.clientWidth;
        var menuwidth=screenwidth*0.75;
        var coinwidth= (menuwidth-30)/3 - 5;
        menuwidth +=  7;
        //var left =  (screenwidth - menuwidth)/2-12;
        //$().message(menuwidth.toString());
        var left =  screenwidth * 0.1; 
        $('#demo_box').popmenu({
                'controller': true,       // use control button or not
                'width': menuwidth+'px',        // width of menu 
                'background': '#34495e',  // background color of menu
                'focusColor': '#1abc9c',  // hover color of menu's buttons
                'borderRadius': '10px',   // radian of angles, '0' for right angle
                'top': '0',              // pixels that move up
                'left': '-'+left,              // pixels that move left
                'iconSize': coinwidth+'px',       // size of menu's buttons
                'color': '#fff',            // color of menu's text
                'border': '1px solid #000' // border style for the menu box
            });
     });
      
    // $( "#id_user_portrait" ).draggable();
