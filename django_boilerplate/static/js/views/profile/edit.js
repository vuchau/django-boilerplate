define(['underscore', 'jquery'], function(_, $){
    var doPasswordsMatch = function(pass1, pass2) {
        var passwordsMatch = true;
        if (pass1 && pass2) {
            if (pass1 != pass2) {
                passwordsMatch = false;
            }
        }
        return passwordsMatch;
    };

    var updateClass = function(els, passwordsMatch) {
        if (!_.isArray(els)) {
            //  force to be an array
            els = [els];
        }
        _.each(els, function(el){
            if (passwordsMatch) {
                el.removeClass('input-error');
            }else{
                el.addClass('input-error');
            }
        });
    };

    var checkNewPasswords = _.debounce(function() {
        var pass1 = $('#id_new_password1'),
            pass2 = $('#id_new_password2');

        var passwordsMatch = doPasswordsMatch(pass1.val(), pass2.val());
        updateClass([pass1, pass2], passwordsMatch);
    }, 500);

    var watchPasswords = function() {
        $('#id_new_password1, #id_new_password2').on('keyup', function(){
            checkNewPasswords();
        });
    };

    return {
        doPasswordsMatch: doPasswordsMatch,
        updateClass: updateClass,
        checkNewPasswords: checkNewPasswords,
        watchPasswords: watchPasswords
    };
});