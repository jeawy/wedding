
$(document).ready(function() {
     
    /***************************************************************************
    submit new user informations section
    *************************************************************************/
    $('#i_upload').click(function(e) {
        e.preventDefault();

        var name = $.trim($('#i_portrait').val());
        if (name == '') {
            $('.div_err').append('<label class="err_label" >请添加图像...</label>'); //
            return;
        }

        var data_user_Form = new FormData($('#id_user_form').get(0));
        $('#i_upload').prop('disabled', 'disabled');
        $.ajax({
            url: '/user/save_portrait/',
            type: 'POST',
            enctype: 'multipart/form-data',
            data: data_user_Form,
            processData: false,
            contentType: false,
            success: function(data) {
                $().message(data);
                 
                $('#i_upload').removeAttr('disabled');
            }
        });

    }); 
    
});