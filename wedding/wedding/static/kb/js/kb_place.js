
$(document).ready(function() {  
    $('.location, .menu-map-img').click(function(e) {
        e.preventDefault();
        $('#kb_provice').empty();
         
        $.get('/area/get_provice_list/', {}, function(data) {
            var html = '';
            for (var i = 0; i < data.length;i++){
                html = '<option value="' +data[i]['id']+ '">'
                              +data[i]['short_name'] + '</option>';
                $('#kb_provice').append(html);
            }  
        });
    })

    $(document).on('change','#kb_provice', function( ) {
        
        $('#kb_city').empty();
        $('#kb_county').empty();
        var provinceid= $('#kb_provice').val();
        $.get('/area/get_city_list/', {provinceid:provinceid}, function(data) {
            var html = '';
            html = '<option value="-1">-市-</option>';
            $('#kb_city').append(html);
            for (var i = 0; i < data.length;i++){
                html = '<option value="' +data[i]['id']+ '">'
                              +data[i]['short_name'] + '</option>';
                $('#kb_city').append(html);
            }  
        });
    });

    $(document).on('change','#kb_city', function( ) { 
        $('#kb_county').empty();
        var cityid= $('#kb_city').val(); 
        $.get('/area/get_county_list/', {cityid:cityid}, function(data) {
            var html = '';
            html = '<option value="-1">-区县-</option>';
            $('#kb_county').append(html);
            for (var i = 0; i < data.length;i++){
                html = '<option value="' +data[i]['id']+ '">'
                              +data[i]['short_name'] + '</option>';
                $('#kb_county').append(html);
            }  
        });
    });
    $('.btn-place-select').click(function(e){
        var value_province = $('#kb_provice').val();
        var value_city = $('#kb_city').val();
        var value_county = $('#kb_county').val();

        var text_province = $('#kb_provice option:selected').text();
        var text_city = $('#kb_city option:selected').text();
        var text_county = $('#kb_county option:selected').text();

        var selectid   = value_province;
        var selectname = text_province;
        if ( parseInt(value_city) > -1)
        {
            selectid = value_city;
            selectname = text_city;
        }
        if ( parseInt(value_county) > -1)
        {
            selectid = value_county;
            selectname = text_county;
        }

        $.get('/area/set_locate_session/', {selectid:selectid, selectname:selectname}, function(data) {
             $('#hidlocationid').val(selectid);
             $('.location').text(selectname);
        });
    });
});