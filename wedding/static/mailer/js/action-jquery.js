$(document).ready(function() {

    /******************************************************************************************************************
    regex for email
    ******************************************************************************************************************/
    function isValidEmailAddress(emailAddress) {
        var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
        return pattern.test(emailAddress);
    };

    var tags = $('#id_email').val();
    var tags_list = tags.split(',');
    $('#id_recipients').tagsManager({
        delimiters: [13, 44],
        prefilled: tags_list,
        validator: function(value) {
            if (isValidEmailAddress(value)) {
                $('.err_label').remove();
                return true;
            }
            else {
                $('.div_err_1').append('<label class="err_label" >邮件格式不正确，请重新输入...</label>'); // 
                return false;
            }

        }
    });


    //plugin only allow numeric string
    $(".positive-integer").numeric(
    { decimal: false, negative: false },
     function() {
         alert("Positive integers only");
         this.value = ""; this.focus();
     }
      );


    /****************************************************************************************************
    save the changes or new
    ****************************************************************************************************/
    $("#id_save").click(function(e) {

        var title = $.trim($("#id_title").val());
        var recipients = $.trim($("#id_recipients").tagsManager('tags')); //
        var days = $.trim($("#id_days").val());
        var content = $.trim($("#id_content").val());
        $('.err_label').remove();
        days = parseInt(days);
        if (title.length > 200) {
            $("#id_title").focus();
            $('.div_err_2').append('<label class="err_label" >标题长度不能超过200....</label>'); //
            return;
        }

        if (recipients == '') {

            //only one email
            recipients = $.trim($("#id_recipients").val());
            if (recipients != '') {
                if (isValidEmailAddress(recipients)) {
                    $('.err_label').remove();
                }
                else {
                    $('.div_err_1').append('<label class="err_label" >邮件格式不正确，请重新输入...</label>'); //

                    return;
                }
            }
            else {
                $("#id_recipients").focus();
                $('.div_err_1').append('<label class="err_label" >请输入收信人的邮箱...</label>'); //
                return;
            }

        }


        if (title == '') {
            $("#id_title").focus();
            $('.div_err_2').append('<label class="err_label" >请输入标题...</label>'); //
            return;
        }

        if (days == '') {
            $("#id_days").focus();
            $('.div_err_3').append('<label class="err_label" >请输入你想在多少天后发送此封邮件...</label>'); //
            return;
        }
        else {
            $("#id_days").val(days);
        }

        if (content == '') {

            $("#id_content").focus();
            $('.div_err_4').append('<label class="err_label" >请在下面输入内容...</label>'); //
            return;
        }

        var id   = $('#lastinfo_id').val();
        var page = $('#id_page').val();

        //submit post
        $.post('/mailer/save_lastinfo/', { title: title, recipients: recipients, days: days, content: content, id:id, page:page }, function(result) {
            if (result['status'] == 'OK') {
                $('.div_err_5').append('<label class="err_label" >' + result['MSG'] + '</label>'); //
                var delay = 3000; //delay in milliseconds
                setTimeout(function() { $(window.location).attr('href', '/mailer/index_lastinfo/'); }, delay);
            }
            else {
                $('.div_err_5').append('<label class="err_label" >' + result['MSG'] + '</label>'); //
            }
        });
    });
});