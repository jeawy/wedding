
$(document).ready(function() {
    $('#product_se_id').change(function() {
        var product_id = $('#product_se_id').val();
        $("#id_div").empty();
        $.get('/base/get_release_list/', { product_id: product_id }, function(data) {
            jQuery('#release_se_id').empty();
            var release = jQuery.parseJSON(data);
            var i = 0;
            
            for (i = 0; i < release.release_list.length; i++) {
                var id = release.release_list[i].id;
                var optiontext = release.release_list[i].version_text;
                $('#release_se_id').prepend("<option value='" + id + "'>" + optiontext + "</option>");
            }
            $('#release_se_id').prepend("<option value='-1'>---------------</option>");
        });
    });

    $('#product_se_id').change(function () {
        var release_id = $('#release_se_id').val();
        $("#id_div").empty();
        $.get('/base/get_component_list/', { release_id: release_id }, function (data) {
            jQuery('#release_se_id').empty();
            var component = jQuery.parseJSON(data);
            var i = 0;

            for (i = 0; i < component.component_list.length; i++) {
                var id = component.component_list[i].id;
                var optiontext = component.component_list[i].version_text;
                $('#release_se_id').prepend("<option value='" + id + "'>" + optiontext + "</option>");
            }
            $('#release_se_id').prepend("<option value='-1'>---------------</option>");
        });
    });

    var wrapper = $(".input_component_wrap"); //
    var add_button = $(".add_component_button"); //

    $(add_button).click(function(e) { //on add input button click

        e.preventDefault();
        var component_text = $("#component_name_id").val(); //
        
        if (component_text == "") {
            $().message("please input component name !");
        }
        else
        {
                var release_id = $("#release_se_id").val(); //
                $(wrapper).append("<div><input type='text' readonly='readonly' name='component_list_text' value='"
                               + component_text + "'/><a href='#' class='remove_field'> Remove"
                            + "</a><input type='Hidden' name='component_list_id' value='"
                            + release_id + "'/></div>"); //add input box;
                $("#component_name_id").val("");
            }
            });
       
    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
    })


    /***************************************************************************
    submit informations section
    *************************************************************************/
    $('#id_submit').click(function(e) {
        e.preventDefault();
        var data_component_Form = new FormData($('#component_form').get(0));
      /*  var component_list_text = $('input[name="component_list_text"]').map(function() {
            return this.value
        }).get()
        var release = $("#release_se_id").val(); //*/
        $.ajax({
        url: '/base/save_components/',
            type: 'POST',
            data: data_component_Form,
            processData: false,
            contentType: false,
            success: function(data) {
                var str = data.toString();
                if (str.length > 1) {
                    if (str[0] == "y")//the issue No is correct in the Zendesk
                    {
                        $().message(str.substr(1, str.length - 1));
                    }
                    else {
                        $().message(str.substr(1, str.length - 1));
                    }
                }
                else {
                    $().message("Error in server side!");
                }
            }
        });
    });
});