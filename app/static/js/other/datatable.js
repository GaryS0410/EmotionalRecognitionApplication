function createDataTable(table) {
    $(document).ready(function () {
        $(table).DataTable({
            searching: false,
            info: false,
            lengthChange: false,
            pageLength: 5,
            responsive: true,
            orderable: false,
            "pagingType": "full_numbers"
        })
    })
}