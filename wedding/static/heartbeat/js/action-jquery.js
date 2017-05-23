$(document).ready(function() {
$('#id_submit').click(function(event) {
    event.preventDefault();
    var words =$.trim($("#idwords").val());
    if (words == '')
    {
        $().message("请输入点什么吧...");
        return;
        }
    $('#id_submit').prop('disabled', 'disabled');
    $.post('/heartbeat/save/', { words: words }, function(data) {
            $().message(data);
            $('#id_submit').removeAttr('disabled');
            var delay = 3000; //delay in milliseconds
            setTimeout(function() { $(window.location).attr('href', '/heartbeat/'); }, delay);
        });
    });
});