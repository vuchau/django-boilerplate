/**
Modalize all data-modal links with #mainModal
*/

define(['jquery', 'foundation'], function($){
    var modal = $('#mainModal'),
        modalSizeClasses = ["tiny", "small", "medium", "large", "xlarge", "full"];
    return function() {
        $(document).on('click', '[data-modal="mainModal"]', function(event){
            event.preventDefault();
            var target = $(event.currentTarget),
                modalSize = target.data('modal-size') || 'medium';
            $.ajax({
                url: target.data('url'),
                method: 'GET',
                success: function(res) {
                    modal.removeClass(modalSizeClasses);
                    modal.addClass(modalSize);
                    modal.find('[data-body]').html(res);
                    if (!modal.is(":visible")) {
                        modal.foundation('reveal', 'open', {
                            animation: 'none',
                            animation_speed: 0
                        });
                    }
                }
            });
        });
    };
});

