(function() {
    // setting a few classes on load
    $('#id_activity_type').addClass("form-control");

    // datepicker initialization
    $('#id_activity_date').datepicker({ autoclose: true, format: 'yyyy-mm-dd' });
    $('#id_start_date').datepicker({ autoclose: true });
    $('#id_end_date').datepicker({ autoclose: true });
    $('.description').tooltip();

  
    // logic for redmine ticket autofill
    var ticket_field = $('#id_ticket_number');
    var description_field = $('#id_description');
    $(ticket_field).on('change', function(){
        if (this.value && this.value != '0') {
            console.log("fetching data..");
            NProgress.start();
            $.get('/redmine/?ticket=' + this.value, function(data){ 
                if (data.status == 200) {
                    $(description_field).val(data.ticket.subject);
                } else {
                    $(description_field).val("Invalid Ticket number!");
                }
                NProgress.done();
            });
        };
    });


    // setting up dataTables
    var dataTable_config = {
        // common datatable config to be used across tables
        "bPaginate" : false,
        "bFilter": false,
        "bInfo": false,
    }


    var seven_day_table = $('#seven_day_table');
    var activities_table = $('#activities_table');
    var todays_table = $('#todays_table');

    if (seven_day_table) {
        $(seven_day_table).dataTable(dataTable_config);
    }

    if (activities_table) {
        $(activities_table).dataTable(dataTable_config);
    }

    if (todays_table) {
        $(todays_table).dataTable(dataTable_config);
    }

})();
