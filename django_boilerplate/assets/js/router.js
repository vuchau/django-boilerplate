/**
Route pages with js functionalities
*/

define(['underscore', 'backbone.marionette',
        'controllers/general',
        'controllers/profile'],
        function(_, Marionette,
                 GeneralController,
                 ProfileController){

    //  all controllers must be listed here
    var controllers = [
            GeneralController,
            ProfileController
        ],
        routes = {};

    //  add routes
    _.each(controllers, function(controller){
        _.each(controller, function(view){
            routes[view.path] = view.method;
        });
    });

    return Marionette.AppRouter.extend({
        routes: routes,
    });
});