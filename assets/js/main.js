
function initRequests () {
    var $oldTable = $('#id_requests_table');

    $.ajax({
        type: 'GET',
        url: '/requests/',
        success: function(data, status, xhr){
            var $newTable = $(data).find('#id_requests_table');
            if ($newTable.html() !== $oldTable.html()) {
                $oldTable.html($newTable.html());
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
