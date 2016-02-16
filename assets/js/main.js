
var $pageTitle = $('title').text();
var windowIsActive;

$(window).focus(function (){
    windowIsActive = true;
});

$(window).blur(function (){
    windowIsActive = false;
});


function initRequests () {
    var $oldTable = $('#id_requests_table');
    var $lastRequestOnPage = $oldTable.find('tr td:first()').html()
    var currentUrl = location.href;

    $.ajax({
        type: 'GET',
        url: currentUrl,
        success: function(data, status, xhr){
            var $newTable = $(data).find('#id_requests_table');
            var $lastRequestInDb = $newTable.find('tr td:first()').html()
            var diff = $lastRequestInDb - $lastRequestOnPage;
            if (diff) {
                if (windowIsActive) {
                    $oldTable.html($newTable.html());
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
