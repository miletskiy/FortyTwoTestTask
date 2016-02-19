
function initUpdateContact () {

    function disableForm() {
        // body...
    };
    function enableForm() {
        // body...
    };

    var options = {
        dataType: 'json',
        beforeSubmit: function(form, options) {
            // body...
            disableForm();
        },
        success: function() {
            enableForm();
            console.log('success');
            $('#id_successMsg').slideDown('slow');
            setTimeout(function() {
                $('#id_successMsg').slideUp('slow');
            }, 4200);
        },
        error: function() {
            console.log('error');
            enableForm();
            $('#id_errorMsg').slideDown('slow');
            setTimeout(function() {
                $('#id_errorMsg').slideUp('slow');
            }, 4200);
        }
    };


    $("#id_edit_form").ajaxForm(options);

};

$(document).ready(function () {
    // body...
    initUpdateContact();
});
