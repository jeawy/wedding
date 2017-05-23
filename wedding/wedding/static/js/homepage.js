
 var jssor_1_SlideoTransitions = [
              [{b:-1,d:1,o:-1},{b:0,d:1000,o:1}],
              [{b:1900,d:2000,x:-379,e:{x:7}}],
              [{b:1900,d:2000,x:-379,e:{x:7}}],
              [{b:-1,d:1,o:-1,r:288,sX:9,sY:9},{b:1000,d:900,x:-1400,y:-660,o:1,r:-288,sX:-9,sY:-9,e:{r:6}},{b:1900,d:1600,x:-200,o:-1,e:{x:16}}]
            ];

            var jssor_1_options = {
              $AutoPlay: false, 
              $SlideDuration: 800,  
              $SlideEasing: $Jease$.$OutQuint,
              $CaptionSliderOptions: {
                $Class: $JssorCaptionSlideo$,
                $Transitions: jssor_1_SlideoTransitions
              } ,
              $BulletNavigatorOptions: {
                $Class: $JssorBulletNavigator$,
                $Scale:false,
                 $AutoCenter: 1,
              }
            };
     
     jQuery(document).ready(function ($) {
            var width = $('.container')[0].clientWidth-30; 
            var height = 0;
            if (width > 900)
            {
                 $('#echarts-map').css({'width':'650px', 'height':'450px'});
                 $('#main').css({'width':'500px', 'height':'300px'});
                 $('.slider1').css({'background':'url("/static/img/homepage/food-wallpaper.jpg") right center / contain no-repeat rgba(155, 163, 160, 0.2)'});
                 height =  width/3;
            }
            else{
                 height = width/2 - 50;
                 $('#echarts-map').css({'width':'450px', 'height':'350px'});
                 $('#main').css({'width':'380px', 'height':'200px'});
                 $('.slider1').css({'background':'url("/static/img/homepage/food-wallpaper.jpg") right top / contain no-repeat rgba(155, 163, 160, 0.2)'});
            }
            //var height = $(window).height()/3*2;
             
            $('#slider1_container').css({'width': width.toString()+'px'});
            $('.slider1_container_child').css({'width': width.toString()+'px'}); 

            $('#slider1_container').css({'height': height.toString()+'px'});
            $('.slider1_container_child').css({'height': height.toString()+'px'}); 
            var jssor_1_slider = new $JssorSlider$("slider1_container", jssor_1_options);
            $('.slider1').css({'left': '14px'});
            $('.slider2').css({'left': '14px'}); 
 
            /*responsive code begin*/
            /*you can remove responsive code if you don't want the slider scales while window resizing*/
           
            /*responsive code end*/
        });