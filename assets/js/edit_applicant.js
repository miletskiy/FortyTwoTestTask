
function initUpdateContact () {

    function disableForm() {
        $('input').attr('disabled',true);
        $('textarea').attr('disabled',true);
        $('#id_indicator').slideDown();
        $('#id_background_layer').show();
    };

    function enableForm() {
        $('input').removeAttr('disabled');
        $('textarea').removeAttr('disabled');
        $('#id_indicator').slideUp('fast');
        $('#id_background_layer').hide();
    };

    var options = {
        dataType: 'json',
        beforeSubmit: function() {
            $('label').removeClass('errorlist');
            $('span:contains("*")').remove();
            disableForm();
        },
        success: function() {
            enableForm();
            $('#id_successMsg').slideDown('slow');
            setTimeout(function() {
                $('#id_successMsg').slideUp('slow');
            }, 4200);
        },
        error: function(response) {
            enableForm();
            $('#id_errorMsg').slideDown('slow');
            setTimeout(function() {
                $('#id_errorMsg').slideUp('slow');
            }, 4200);
            var errors = JSON.parse(response.responseText);
            var id, errorMessage, $idElement,$labelElement;
            for(error in errors) {
                id = '#id_' + error;
                $idElement = $(id);
                errorMessage = errors[error];
                $idElement.addClass('errorlist').val(errorMessage);

                $labelElement = $("label[for='"+$idElement.attr('id')+"']")
                $labelElement.addClass('errorlist').prepend('<span>*</span>');

                $('span').addClass('errorlist');

                $('.errorlist').focus(function() {
                        $(this).val('').removeClass('errorlist');
                });
            };
        }
    };


    $("#id_edit_form").ajaxForm(options);

};

$(document).ready(function () {
    initUpdateContact();
});
