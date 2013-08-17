// Defining the tour!

var tour = {
    id: 'dashboard-tour',
    steps: [
        {
            title: 'The form!',
            content: 'This is the form which you can use to add new activities',
            target: "new_activity_form",
            placement: 'right'
        },
        {
            title: 'Recent Activites - Today!',
            content: 'This is a table showing you a list of activities that you added today',
            target: "today_activities_table",
            placement: 'left'
        },
        {
            title: 'Recent Activites - Last 7 days!',
            content: 'This is a table showing you a list of activities that you added in the last seven days',
            target: "last_seven_activities_table",
            placement: 'top'
        },
        {
            title: 'More Entires?',
            content: 'Click here to see a list of all activities that you have added',
            target: "more_entries_button",
            placement: 'top'
        }
    ]
}

// Start the tour!
$('#begin_tour').on('click', function() {
    hopscotch.startTour(tour);
});
