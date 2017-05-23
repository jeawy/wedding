$(document).ready(function(){
   // 添加地名
   $('.btn-add-place').click(function(){
     
        var placename = $('#kb_county option:selected').text();
        var placeid   = $('#kb_county option:selected').val();

        if (placeid == undefined || placeid == '-1')
        {
             placename = $('#kb_city option:selected').text();
             placeid   = $('#kb_city option:selected').val();
             if (placeid == undefined || placeid == '-1')
              {
                  placename = $('#kb_provice option:selected').text();
                  placeid   = $('#kb_provice option:selected').val();
              }
        }   
        var addin = false;
        $('.placeid_list').each(function(index){
              if ($(this).val() == placeid)
              {
                addin = true;
                return;
              } 
        });
       if (  addin == false)
       {
          var html ='';
          html += '<div class="col-xs-2 col-sm-2"> '+
              '<div class="alert alert-success fade in m-b-1">'+  
                        '<label >'+placename+'</label>' +  
                         '<input type="hidden" class="placeid_list" value="'+placeid+'" >'+  
                  '<span class="close close-place" data-dismiss="alert">&times;</span>' +
            '</div> '+
          '</div>';

          $('.row-place').append(html);
        }
 
   });
   $(document).on('click', '.close-place', function(){
      $(this)[0].parentElement.parentElement.remove();
   });

   // 添加推荐饭店
   $('.btn-add-address').click(function(){
        var place   = $('.place_go').val();
        var html ='';
        var tmp = ""; 
        var addin = false;
        $('.address_list').each(function(index){
            tmp = $.trim($(this).text());
            if(tmp == place)
            {
               addin = true;
              return;
            }
        });
        if (  addin == false)
        {
          html +=  '<div class="col-xs-12 col-md-12" >' +
                  '<div class="alert alert-success fade in m-b-15"> '+  
                  ' <label class="address_list">'+place+' </label>  '+
                        '<span class="close" data-dismiss="alert">&times;</span>'+
                  '</div> '+
                  '</div>';

          $('.row-addresses').append(html); 
          $('.place_go').val('');
        }
   });

   //发布
   $('.btn-publish').click(function(e){
     var kbid = $.trim($('#id_kbid').val());
     var price_lower = $.trim($('#price_lower').val());
     if (price_lower != '')
     {
         if ( ! $.isNumeric(price_lower))
         {
           $('#price_lower').parent().addClass('has-error');
           $('#price_lower').focus();
           $().errormessage('价格必须是数字');
           $('#price_lower').val('');
           return;
         }
     }
     var price_higher = $.trim($('#price_higher').val());
     if (price_higher != '')
     {
         if ( ! $.isNumeric(price_higher))
         {
           $('#price_higher').parent().addClass('has-error');
           $('#price_higher').focus();
           $().errormessage('价格必须是数字');
           $('#price_higher').val('');
           return;
         }
     }
      var locations =[];
      var placeid_list = $('.placeid_list');
      if (placeid_list.length == 0)
      {
          var county =  $('#kb_county option:selected').val();
          if (county != undefined && county != '-1' )
          {
            locations.push(county);
          }
          else{
            var city =  $('#kb_city option:selected').val();
            if (city != undefined && city != '-1')
            {
                  locations.push(city);
            }
            else
            {
                locations.push($('#kb_provice option:selected').val());
            }
          }
      }
      else{
        placeid_list.each(function(index){
              locations.push($(this).val());
        });
      }

     var places =[];
      var address_list = $('.address_list');
      if (address_list.length == 0)
      {
          if ($.trim($('.place_go').val()) == "" ){
            $('.place_go').parent().addClass('has-error');
            $('.place_go').focus();
            $().errormessage('请告诉小伙伴们如何才能品尝到这份美食...');
            return;
          }
          else{
            places.push( $.trim($('.place_go').val()) );
          }
      }
      else{
        address_list.each(function(index){
              places.push($(this).text());
        });
      }
      $.isLoading({ text: "请稍后..." }); 
      $.post('/kb/publish_kb/', {kbid:kbid, lower_price:price_lower, 
        higher_price:price_higher, places:places,  locations:locations}, function(result){
          $.isLoading('hide');
          if (result['status'] == 4)
          {
              $.confirm({
                text:"Wow， 发布成功...",
                confirmButton:'去看看',
                cancelButton:'继续编辑',
                confirm:function(){
                  window.location.href='/kb/'+kbid+'/kb_detail/';  
                },
                cancel: function() { 
                  location.reload();
                        }
              }); 
 
          }
          else
          {
            $().errormessage(result['msg']);
          }
      });
   });


   $('#price_lower, #price_higher').keyup(function(){
        $(this).parent().removeClass('has-error');
   });
});