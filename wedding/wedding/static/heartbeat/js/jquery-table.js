
$(document).ready(function() {
$('#data-table-list').DataTable({
    "order": [
                [0, "desc"]
        ],
    "columnDefs": [
                {
                    "scrollY": 200,
                    "scrollCollapse": true,
                    "jQueryUI": true
                }
            ]
});

});