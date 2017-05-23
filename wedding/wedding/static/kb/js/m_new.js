$(document).ready(function() {
    /*
    $.datepicker.setDefaults($.datepicker.regional['zh']);
   //$('#id_birthday').datepicker({    minDate: 0,  });
   $('#deadline').datepicker( {dateFormat: "yy-mm-dd",
    changeMonth: true,
     minDate: 0,
   }); 
   */
    $(document).on('touchstart', ".fa-heart", function() {
        event.preventDefault();
        var current = $(this);

        var is_authenticated = $('#login').val();
        if (is_authenticated == 0) {
            $().message('请先登录...');
            var delay = 3000; //delay in milliseconds
            setTimeout(function() { $(window.location).attr('href', '/login/'); }, delay);
            return;
        }
        var day_words_id = current.parent().find('.word_id').val()
        var count = current[0].outerText;
        count = parseInt(count);
        if (count <= 0)
            return;

        $.post('/good/del/', { day_words_id: day_words_id }, function(data) {
            var status = data['status'];
            var msg = data['msg'];

            if (status == '1') {
                $().message(msg);
                var delay = 3000; //delay in milliseconds
                setTimeout(function() { $(window.location).attr('href', '/login/'); }, delay);
            }
            else {
                if (status == '0') {
                    current.removeClass('fa-heart');
                    current.addClass('fa-heart-o');
                    current.text(count - 1);
                }
                else {
                    $().message(msg);
                }
            }

        });
    });
    var classname = 'pic_holder_';
    $('#id_add_pic_text').click(function(event) {
        var idslice_count = $('#idslice_count').val();

        idslice_count = parseInt(idslice_count) + 1;
        $('#idslice_count').val(idslice_count);
        var html = '<li>' +
            '<textarea class="form-control article_content" name="article_content_' + idslice_count.toString() + '"  cols="30" rows="10"></textarea></li>' +
      '<li class="li_holder"></li>' +
       '<li class="li_pic_add_div"> <input type="hidden" class ="slice_number" name="slice_number_' + idslice_count.toString()
       + '" value="' + idslice_count.toString() + '" /><input type="hidden" name="kb_slice_instace_' + idslice_count.toString() 
       + '" id ="id_kb_slice_' + idslice_count.toString() + '" value="0" /><div class="pic_add_div">' +
       ' <label class="new_Btn"><input type="file" name="pic_file"   class="file_upload"  accept="image/*"/> ' +
                      '<i class="fa fa-plus pic-plus"></i> </label></div></li>';
        var append_selector = $(this)[0].parentElement.previousElementSibling;
        $(append_selector).after(html); 
    });


    /* delete picture
    */
    $(document).on('touchstart', ".pic-delete", function(event) {
        var curren = $(this);
        var picid = $($(this).context.previousElementSibling).val();

        $.post('/kb/del_pic/', { picid: picid }, function(data) {
            $(curren.context.parentElement).remove();
        });
    });
    $(document).on('click', ".pic-delete", function(event) {
        var curren = $(this);
        var picid = $($(this).context.previousElementSibling).val();
        $().message('touched');
        $.post('/kb/del_pic/', { picid: picid }, function(data) {
            $(curren.context.parentElement).remove();
        });
    });


    $(document).on('change', ".file_upload", function() {
        //event.preventDefault(); 

        var current = $(this);
        //current slice number
        var slice_num = $(current[0].parentElement.parentElement.parentElement).find('.slice_number').val()



        var idslice_count = $('#idslice_count').val();
        var id_kb_slice_selector = '#id_kb_slice_' + slice_num.toString();
        var id_kb_slice = $(id_kb_slice_selector).val();
        var id_kb = $('#id_kb').val();

        var idblock = $('#idblock').val();


        var formData = new FormData();
        formData.append("imagefile", current[0].files[0]);
        formData.append("id_kb_slice", id_kb_slice);
        formData.append("id_kb", id_kb);
        formData.append('type', $('#idtype').val());
        formData.append("idblock", idblock);


        //get the parent picture holder
        var currnet_li_holder = current[0].parentElement.parentElement.parentElement.previousElementSibling;

        var count = current[0].outerText;
        count = parseInt(count);
        if (count <= 0)
            return;

        $.ajax('/kb/upload_image/', {
            method: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                if (data['status'] == 'OK') {
                    var newclassname = classname + data['id_pic'];
                    var newplaceholder = '<div class="pic_holder ' + newclassname + '">  ' +
                                           '<input type="hidden" class="pic_id" value="' + data['id_pic'] + ' " />' +
                                            ' <i class="fa fa-minus-circle pic-delete"></i>' +
                                        '</div>';
                    $(currnet_li_holder).append(newplaceholder);
                    data['file'] = data['file'].replace('\\', '/');
                    $('.' + newclassname).css("background-image", "url(" + data['file'] + ")");
                    $(id_kb_slice_selector).val(data['id_kb_slice']); //id_kb_slice
                    $('#id_kb').val(data['id_kb']);
                }
                else {
                    $('.div_err').append('<label class="err_label" >' + data['msg'] + '</label>'); //
                }
            },
            error: function() {
                console.log('Upload error');
            }
        });
    });


 $('#id_publish_draft').click(function(event) {
     event.preventDefault(); 
     $('#id_publish_draft').attr('disabled', 'disabled');
     $.confirm({
        text: "文章已存为草稿，还需要进一步编辑才可以发布...",
        confirmButton: "去看看帖子",
        cancelButton: "去设置顶图",
        dialogClass: "modal-dialog",
        confirm: function() {
            $().message('confirm');
        },
        cancel: function() {
            $().message('cancel');
        }
});

// window.location.href = '/'; 
 });
 
    $('#id_publish').click(function(event) {

        var title = $.trim($('#id_title').val());
        if (title == '') {
            $('.li_title').append('<label class="errornote" >标题不能为空</label>'); //
            return;
        }
        var selector_active_num = $('#active_num');
        if (selector_active_num.length != 0)
        {
            var num = $.trim($('#active_num').val());
            if (num == '') {
                $('.li_active').append('<label class="errornote" >请输入活动上限人数</label>'); //
                return;
            }
        }
        
        var selector_money = $('#id_money');
        if (selector_money.length != 0)
        {
            var money = $.trim($('#id_money').val());
            if (money == '') {
                $('.li_active').append('<label class="errornote" >请输入活动上限人数</label>'); //
                return;
            }
            else{
                if( isNaN(parseInt(money)))
                {
                    $('.li_active').append('<label class="errornote" >请输入数字...</label>'); //
                return;
                }
            }
        }
        
        var selector_deadline = $('#deadline');
        if (selector_deadline.length != 0)
        {
            var deadline = $.trim($('#deadline').val());
            if (deadline == '') {
                $('.li_active').append('<label class="errornote" >请输入活动截止日期.</label>'); //
                return;
            }
        }
        $('#id_publish').attr('disabled', 'disabled');
        var formData = new FormData($('#article_form').get(0));
        $.ajax('/kb/savekb/', {
            method: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                if (data['status'] == 'OK') { 
                    var kbid = data['id'];
                    /*
                    $.confirm({
                        text: "文章已存为草稿，还需要进一步编辑才可以发布...",
                        confirmButton: "暂不",
                        cancelButton: "下一步",
                        dialogClass: "modal-dialog",
                        confirm: function() {
                            //去查看帖子详情
                             window.location.href = '/kb/'+kbid+'/kb_detail/'; 
                        },
                        cancel: function() {
                            //去设置顶图
                             window.location.href = '/kb/'+kbid+'/set_kb_top_pic/'; 
                        }
                    });
                    */
                    window.location.href = '/kb/'+kbid+'/set_kb_top_pic/'; 
                }
                else {
                    $('.publish_msg').append('<label class="noteerror" >' + data['msg'] + '</label>'); //
                }
            },
            error: function() {
                console.log('Upload error');
            }
        });
    });
});