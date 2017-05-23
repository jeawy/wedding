$(document).ready(function() {
    $('#delete').click(function(event) {
        event.preventDefault();

        var id = $.trim($("#heartbeat_id").val());
         
            $('#delete').prop('disabled', 'disabled');

            $.post('/heartbeat/do_delete/', { id: id }, function(data) {
                $().message(data);
                var delay = 3000; //delay in milliseconds
                setTimeout(function() { window.location="/heartbeat/"; }, delay);
            });
    });
    
    $('#cancel').click(function(event) {
        event.preventDefault();
        var delay = 100; //delay in milliseconds
        setTimeout(function() { history.back(); }, delay);
       
    });
});