$(document).ready(function() {
   $.datepicker.setDefaults($.datepicker.regional['zh']);
   $('#deadline').datepicker( {dateFormat: "yy-mm-dd",
    changeMonth: true,
     minDate: 0,
   });  
});