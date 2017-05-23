
$(document).ready(function() {
    /***************************************************************************
    submit fix informations section
    *************************************************************************/
      $('#id_submitTicket').click(function(e) {
        event.preventDefault();
        var data_ticket_Form = new FormData($('#ticket_form').get(0));
        var isFinished = $('#id_checkbox').prop('checked')  // Boolean true
        $('#id_submitTicket').prop('disabled', 'disabled');
        if (typeof isFinished === "undefined") { isFinished = false }
        data_ticket_Form.append('isFinished', isFinished);
        $.ajax({
            url: '/ticket/saveticket/',
            type: 'POST',
            data: data_ticket_Form,
            processData: false,
            contentType: false,
            success: function(data) {
            $().message(data);
                $('#id_submitTicket').removeAttr('disabled');
                 var delay = 3000; //delay in milliseconds
                 setTimeout(function() { history.back(); }, delay);
            }
        });
    });
});