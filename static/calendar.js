function populateUnavailableDates(unavailable_dates) {
  var unavailableDates = [];

  for (var i = 0; i < unavailable_dates.length; i++) {
    var date = unavailable_dates[i];
    unavailableDates.push({
      title: 'Unavailable',
      start: date.start_date,
      end: date.end_date,
      available: false
    });
  }

  return unavailableDates;
}

$(document).ready(function() {
  var startDate = null; 
  var endDate = null; 

  $.ajax({
    url: '/get-dates',
    method: 'GET',
    success: function(response) {
     // var unavailableDates = populateUnavailableDates(response.unavailable_dates);
      renderCalendar();
    },
    error: function(xhr, status, error) {
      console.error(error);
    }
  });
  function renderCalendar() {
    var startDate = null;
    var endDate = null;
  
    $('#calendar').fullCalendar({
      selectable: true,
      longPressDelay: 0,
      select: function (start, end) {
        var today = moment().startOf('day');
        if (startDate === null) {
          startDate = start;
          if (startDate.isBefore(today)) {
            // Ignore the selection
            $('#selectedDates').text('Please select a future start date.');
            startDate = null;
            return;
          }
  
          $('#startDate').val(startDate.format('YYYY-MM-DD'));
          $('#selectedDates').text('Selected Start Date: ' + startDate.format('YYYY-MM-DD'));
        } else if (endDate === null && end.isAfter(startDate)) {
          endDate = moment(end).subtract(1, 'day'); 
          var numDays = Math.abs(endDate.diff(startDate, 'days')) + 1;

          $('#endDate').val(endDate.format('YYYY-MM-DD'));
          $('#numDays').val(numDays);
          $('#selectedDates').html('Selected start date: ' + startDate.format('YYYY-MM-DD') +
            '<br>Selected end date: ' + endDate.format('YYYY-MM-DD') +
            '<br>Number of days: ' + numDays);
          startDate = null;
          endDate = null;
        } else {
          $('#selectedDates').text('Invalid date selection. Please choose again.');
          startDate = null;
          endDate = null;
        }
      },  
  
      eventRender: function(event, element) {
        if (event.available) {
          element.css('background-color', 'green');
        } else {
          element.css('background-color', 'red');
        }
      },
       // events: unavailableDates
    });
  }});
