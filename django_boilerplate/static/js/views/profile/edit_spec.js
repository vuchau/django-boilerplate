define(['jquery', './edit'], function($, edit){
    describe('Edit Profile', function() {
        describe('doPasswordsMatch()', function () {
            it('should be true if either passwords doesn\'t exist or they match', function () {
                assert.isTrue(edit.doPasswordsMatch('foo', 'foo'));
                assert.isTrue(edit.doPasswordsMatch('', ''));
                assert.isTrue(edit.doPasswordsMatch('', 'bar'));
                assert.isTrue(edit.doPasswordsMatch(null, 'baz'));
                assert.isTrue(edit.doPasswordsMatch(null, null));
                assert.isFalse(edit.doPasswordsMatch('foo', 'bar'));
            });
        });
        describe('doPasswordsMatch()', function () {
            it('element should have input-error class if passwords don\'t match', function () {
                var el = $('<div></div>');
                edit.updateClass(el, true);
                assert.isFalse(el.hasClass('input-error'));
                edit.updateClass([el], true);
                assert.isFalse(el.hasClass('input-error'));
                edit.updateClass(el, false);
                assert.isTrue(el.hasClass('input-error'));
                edit.updateClass([el], false);
                assert.isTrue(el.hasClass('input-error'));

                el.addClass('foo');
                edit.updateClass(el, true);
                assert.isFalse(el.hasClass('input-error'));
                assert.isTrue(el.hasClass('foo'));
                edit.updateClass(el, false);
                assert.isTrue(el.hasClass('input-error'));
                assert.isTrue(el.hasClass('foo'));
            });
        });
    });
});