requirejs.config({
    baseUrl: '/static/js',
    paths: {
        jquery: '../bower_components/jquery/dist/jquery',
        underscore: '../bower_components/underscore/underscore',
        backbone: '../bower_components/backbone/backbone',
        'backbone.marionette': '../bower_components/backbone.marionette/lib/backbone.marionette',
        foundation: '../bower_components/foundation/js/foundation'
    },
    shim: {
        "foundation": ['jquery'],
    }
});

require(['jquery', 'foundation'], function ($) {
    $(document).ready(function(){
        $(document).foundation();

        //  modalize all data-modal links with #mainModal
        $('[data-modal]').on('click', function(event){
            event.preventDefault();
            var target = $(event.currentTarget);
            $.ajax({
                url: target.data('modal'),
                method: 'GET',
                success: function(res) {
                    $('#mainModal').find('[data-body]').html(res);
                    $('#mainModal').foundation('reveal', 'open');
                }
            });
        });
    });
});