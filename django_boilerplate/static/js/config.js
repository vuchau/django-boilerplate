/**
Main front-end configuration
*/

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

require(['app'], function(app) {
    $(document).ready(function(){
        app.start();
    });
});