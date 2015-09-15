/**
Main Marionette application
*/

define(['jquery', 'backbone', 'backbone.marionette',
        'analytics', 'router', 'modal', 'foundation'],
        function($, Backbone, Marionette, Analytics, AppRouter, modalize){
    var app = new Marionette.Application();

    app.addInitializer(function(options) {
        // var analytics = new Analytics();
        var router = new AppRouter();
        Backbone.history.start({pushState: true});
    });

    app.on("start", function(){
        $(document).foundation();
        modalize();
    });

    return app;
});