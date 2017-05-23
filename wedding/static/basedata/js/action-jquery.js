$(document).ready(function() {
$('#id_submit').click(function(event) {
    event.preventDefault();
    var words =$.trim($("#idwords").val());
    if (words == '')
    {
        $().message("请写入你要推荐的内容...");
        return;
        }
    $('#id_submit').prop('disabled', 'disabled');

    $.post('/base/save_day_words/', { words: words }, function(data) {
            $().message(data);
            var delay = 3000; //delay in milliseconds
            setTimeout(function() { $(window.location).attr('href', '/'); }, delay);
        });
    });

});