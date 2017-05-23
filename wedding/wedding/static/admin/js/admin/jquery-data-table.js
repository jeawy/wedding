
$(document).ready(function() {
$('#data-table-list').dataTable({ 
        //"dom": '<"toolbar">frtip',
        "columnDefs": [
            {
                "targets": [0],
                "visible": false,
                "scrollY": 200,
                "scrollCollapse": true,
                "jQueryUI": true
            }
        ]
        });
});