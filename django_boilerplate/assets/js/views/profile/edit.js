define(['underscore', 'jquery'], function(_, $){
    var checkNewPasswords = _.debounce(function() {
        var pass1 = $('#id_new_password1'),
            pass2 = $('#id_new_password2'),
            pass1Value = pass1.val(),
            pass2Value = pass2.val(),
            passwordsMatch = true;

        if (pass1Value && pass2Value) {
            if (pass1Value != pass2Value) {
                passwordsMatch = false;
            }
        }

        if (passwordsMatch) {
            pass1.removeClass('input-error');
            pass2.removeClass('input-error');
        }else{
            pass1.addClass('input-error');
            pass2.addClass('input-error');
        }
    }, 500);

    return function() {
        $('#id_new_password1, #id_new_password2').on('keyup', function(){
            checkNewPasswords();
        });
    };
});