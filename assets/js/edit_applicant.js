
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
            $('span:contains("This field is required.")').remove();
            disableForm();
        },
        success: function(data) {

            var photoPath = data.link_file;
            var defaultImage = '/static/img/default.jpg';
            var currently = 'Currently: <a href="/uploads/'+photoPath+'">'+photoPath+'</a>';
            var input = '<input id="photo-clear_id" name="photo-clear" type="checkbox" />';
            var label = '<label for="photo-clear_id"> Clear</label><br />Change: <input id="id_photo" name="photo" type="file" /><br>';
            var img = '<img src="/uploads/'+photoPath+'" alt="Applicant_photo"class="photo_applicant">';
            if (photoPath) {
                $('#id_input_photo').html(currently+input+label);
                $('#id_photo img').attr('src','/uploads/'+photoPath);
            }else{
                $('#id_input_photo').html('<input id="id_photo" name="photo" type="file">');
                $('#id_photo img').attr('src',defaultImage);
            };
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
                $idElement.parent('li').prepend('<span>'+errorMessage+'</span>');
                $labelElement = $("label[for='"+$idElement.attr('id')+"']")
                $labelElement.addClass('errorlist').prepend('<span>*</span>');
                $('span').addClass('errors');
            };
        }
    };


    $("#id_edit_form").ajaxForm(options);

};

$(document).ready(function () {
    initUpdateContact();
});
