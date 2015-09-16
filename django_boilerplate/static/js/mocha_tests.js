requirejs.config({
    baseUrl: '',
    paths: {
        jquery: '../bower_components/jquery/dist/jquery',
        underscore: '../bower_components/underscore/underscore',
        backbone: '../bower_components/backbone/backbone',
        'backbone.marionette': '../bower_components/backbone.marionette/lib/backbone.marionette',
        foundation: '../bower_components/foundation/js/foundation',
        mocha: '../bower_components/mocha/mocha',
        chai: '../bower_components/chai/chai'
    },
    shim: {
        'chai-jquery': [
            'jquery',
            'chai'
        ],
        'mocha': {
            init: function () {
                this.mocha.setup('bdd');
                return this.mocha;
            }
        }
    },
    urlArgs: 'bust=' + (new Date()).getTime()
});

define(['underscore', 'chai', 'mocha'], function (_, chai, mocha) {
    assert = chai.assert;

    //  add your test file paths here
    require([
        'views/profile/edit_spec',
    ], function() {
        if (typeof mochaPhantomJS !== 'undefined') {
            //  run using mocha-phantomjs
            mochaPhantomJS.run();
        }else{
            //  open mocha_index.html directly
            mocha.run();
        }
    });
});