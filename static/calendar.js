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
      var unavailableDates = populateUnavailableDates(response.unavailable_dates);
      renderCalendar(unavailableDates);
    },
    error: function(xhr, status, error) {
      console.error(error);
    }
  });
  function renderCalendar(unavailableDates) {
    $('#calendar').fullCalendar({
      selectable: true, 
      select: function(start, end) {
        if (startDate === null) {
          startDate = start;
          endDate = null;
          $('#startDate').val(startDate.format('YYYY-MM-DD'));
          $('#selectedDates').text('Selected Start Date: ' + startDate.format('YYYY-MM-DD'));
        } else if (endDate === null) {
          endDate = moment(end).subtract(1, 'day'); // Adjust the end date to be inclusive
          var numDays = Math.abs(endDate.diff(startDate, 'days')) + 1;
  
          $('#endDate').val(endDate.format('YYYY-MM-DD'));
          $('#numDays').val(numDays);
          $('#selectedDates').html('Selected start date: ' + startDate.format('YYYY-MM-DD') +
          '<br>Selected end date: ' + endDate.format('YYYY-MM-DD') +
          '<br>Number of days: ' + numDays);      
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
        events: unavailableDates
    });
  }});
