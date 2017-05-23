$(document).ready(function() {


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

        var years = $.trim($("#id_years").val());
        var content = $.trim($("#id_content").val());
        $('.err_label').remove();
       
        if (title.length > 200) {
            $("#id_title").focus();
            $('.div_err_2').append('<label class="err_label" >标题长度不能超过200....</label>'); //
            return;
        }



        if (title == '') {
            $("#id_title").focus();
            $('.div_err_2').append('<label class="err_label" >请输入标题...</label>'); //
            return;
        }

        if (years == '') {
            $("#id_years").focus();
            $('.div_err_3').append('<label class="err_label" >请输入你想在多少年后发送此封邮件...</label>'); //
            return;
        }
        else {
            years = parseFloat(years).toFixed(2);  
            $("#id_years").val(years);
        }

        if (content == '') {

            $("#id_content").focus();
            $('.div_err_4').append('<label class="err_label" >请在下面输入内容...</label>'); //
            return;
        }

        var id   = $('#lastinfo_id').val();
        var page = $('#id_page').val();

        //submit post
        $.post('/mailer/save_tofuture/', { title: title, years: years, content: content, id: id, page: page }, function(result) {
            if (result['status'] == 'OK') {
                $('.div_err_5').append('<label class="err_label" >' + result['MSG'] + '</label>'); //
                var delay = 3000; //delay in milliseconds
                setTimeout(function() { $(window.location).attr('href', '/mailer/' + result['id'] + '/detail_tofuture/'); }, delay);
            }
            else {
                $('.div_err_5').append('<label class="err_label" >' + result['MSG'] + '</label>'); //
            }
        });
    });
});