
function initUpdateContact () {

    function disableForm() {
        // body...
    };
    function enableForm() {
        // body...
    };

    var options = {
        beforeSubmit: function(form, options) {
            // body...
            disableForm();
        },
        success: function() {
            enableForm();
        },
        error: function() {
            enableForm();
        }
    };


    $("#id_edit_form").ajaxForm(options);

};

$(document).ready(function () {
    // body...
    initUpdateContact();
});
