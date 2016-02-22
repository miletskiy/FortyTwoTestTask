
var $pageTitle = $('title').text();
var windowIsActive;

$(window).focus(function (){
    windowIsActive = true;
});

$(window).blur(function (){
    windowIsActive = false;
});

var dateOptions = {
  month: 'short',
  day: 'numeric',
  year: 'numeric',
  hour:'2-digit',
  minute:'2-digit',
};

function initRequests () {
    var $oldTable = $('#id_tbody');
    var $lastRequestOnPage = $oldTable.find('td:first()').html()
    var currentUrl = location.href;

    $.ajax({
        type: 'GET',
        url: currentUrl,
        success: function(data, status, xhr){
            var newTable;
            for (var i = 0; i < data.length; i++) {
                var lastRequestInDb = data[0].pk;
                var date = new Date(data[i].fields.emergence);
                var tableRow = '<tr><td>' + data[i].pk + '</td>';
                tableRow += '<td>' + data[i].fields.title + '</td>';
                tableRow += '<td>' + date.toLocaleString("en-US", dateOptions) + '</td>';
                tableRow += '<td>' + data[i].fields.path + '</td>';
                tableRow += '<td>' + data[i].fields.method + '</td>';
                var user = data[i].fields.user||'None';
                tableRow += '<td>' + user + '</td></tr>';
                newTable +=tableRow;
            };
            var diff = lastRequestInDb - $lastRequestOnPage;
            if (diff) {
                if (windowIsActive) {
                    $oldTable.html(newTable);
                    $('title').text($pageTitle);
                } else {
                    var newTitle = '('+ diff +') '+ $pageTitle;
                    $('title').text(newTitle);
                };
            };
        },
        error: function(){
            console.log('An error occurred!');
        }
    });
};


$(document).ready(function () {
    setInterval(initRequests, 4200);
});
